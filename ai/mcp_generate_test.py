"""
Generate a pytest Playwright-Python test by driving the official Playwright MCP server.

Why this works:
- We connect to the Playwright MCP server over stdio: `npx -y @playwright/mcp@latest`
- We enable test-related MCP tools via: `--caps=testing` (locators + assertions)
  (See Playwright MCP README: test assertions are opt-in via --caps=testing)

Run:
  python tools/mcp_generate_test.py scenarios/login.json

Scenario format (JSON):
{
  "test_name": "login_happy_path",
  "base_url": "https://example.com/login",
  "steps": [
    {"tool": "browser_navigate", "args": {"url": "https://example.com/login"}},
    {"tool": "browser_snapshot"},
    {"tool": "browser_type", "args": {"element": "Username", "ref": "REF_FROM_SNAPSHOT", "text": "demo"}},
    {"tool": "browser_type", "args": {"element": "Password", "ref": "REF_FROM_SNAPSHOT", "text": "secret"}},
    {"tool": "browser_click", "args": {"element": "Sign in", "ref": "REF_FROM_SNAPSHOT"}},
    {"tool": "browser_verify_text_visible", "args": {"text": "Welcome"}}
  ]
}

Notes:
- For click/type tools you must supply a `ref` from `browser_snapshot`.
- If you don’t want to hand-pick refs, you can add your own “AI step”
  that parses the snapshot and selects refs, or build a small helper that searches
  snapshot text patterns.
"""

import asyncio
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from slugify import slugify

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# ----------------------------
# Utilities
# ----------------------------
CODE_BLOCK_RE = re.compile(r"```[a-zA-Z]*\n(.*?)```", re.DOTALL)

def _ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def _extract_code_blocks(text: str) -> List[str]:
    return [m.strip() for m in CODE_BLOCK_RE.findall(text or "")]

def _mcp_text(result: Any) -> str:
    """
    MCP tool results commonly come back as:
      {"content":[{"type":"text","text":"..."}], ...}
    This helper extracts concatenated text parts safely.
    """
    if result is None:
        return ""
    content = getattr(result, "content", None) or result.get("content") if isinstance(result, dict) else None
    if not content:
        return str(result)
    texts = []
    for item in content:
        if isinstance(item, dict) and item.get("type") == "text":
            texts.append(item.get("text", ""))
        else:
            # fall back to string
            texts.append(str(item))
    return "\n".join(texts).strip()


@dataclass
class Scenario:
    test_name: str
    base_url: str
    steps: List[Dict[str, Any]]


def load_scenario(path: Path) -> Scenario:
    data = json.loads(path.read_text(encoding="utf-8"))
    return Scenario(
        test_name=data.get("test_name", path.stem),
        base_url=data["base_url"],
        steps=data.get("steps", []),
    )


# ----------------------------
# MCP driver
# ----------------------------
async def connect_playwright_mcp() -> Tuple[ClientSession, Any]:
    """
    Connect to the official Playwright MCP server via stdio:
      npx -y @playwright/mcp@latest --caps=testing
    """
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@playwright/mcp@latest", "--caps=testing"],
        env=os.environ.copy(),
    )
    # Use async context manager for stdio_client
    # The caller must use: async with connect_playwright_mcp() as (session, transport):
    return stdio_client(server_params)


async def list_tool_names(session: ClientSession) -> List[str]:
    tools = await session.list_tools()
    return [t.name for t in tools.tools]


async def call_tool(session: ClientSession, tool: str, args: Optional[Dict[str, Any]] = None) -> Any:
    args = args or {}
    return await session.call_tool(tool, args)


# ----------------------------
# Codegen (Python pytest)
# ----------------------------
def js_to_python_sync(js_lines: str) -> List[str]:
    """
    Best-effort conversion of tool-emitted JS snippets into Playwright-Python sync-ish lines.
    The MCP server often includes "Ran Playwright code" snippets like: await page.goto('...')
    We convert a few common patterns. You can extend as you like.
    """
    out: List[str] = []
    for raw in (js_lines or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("//"):
            continue

        # remove leading await
        line = line.replace("await ", "")

        # JS -> Python minor transforms
        line = line.replace("page.getByRole", "page.get_by_role")
        line = line.replace("page.getByText", "page.get_by_text")
        line = line.replace("page.locator", "page.locator")
        line = line.replace(".fill(", ".fill(")
        line = line.replace(".click(", ".click(")

        # getByRole('button', { name: 'Sign in' }) -> get_by_role("button", name="Sign in")
        line = re.sub(r"get_by_role\('([^']+)'\s*,\s*\{\s*name:\s*'([^']+)'\s*\}\)",
                      r'get_by_role("\1", name="\2")', line)

        # goto('url') -> goto("url")
        line = re.sub(r"goto\('([^']+)'\)", r'goto("\1")', line)

        # normalize quotes
        line = line.replace("'", '"')

        out.append(line)
    return out


def render_pytest_test(test_name: str, base_url: str, python_steps: List[str]) -> str:
    safe_name = re.sub(r"[^a-zA-Z0-9_]+", "_", test_name).strip("_").lower()
    if not safe_name.startswith("test_"):
        safe_name = "test_" + safe_name

    body = "\n    ".join(python_steps) if python_steps else "pass"

    return f'''import pytest
from playwright.sync_api import Page, expect

@pytest.mark.generated
def {safe_name}(page: Page):
    # Base URL (for reference)
    base_url = "{base_url}"

    {body}
'''


async def run_generation(scenario_path: Path) -> Path:
    scenario = load_scenario(scenario_path)

    async with await connect_playwright_mcp() as transport:
        stdio, write = transport
        session = ClientSession(stdio, write)
        await session.initialize()
        try:
            tool_names = await list_tool_names(session)
            print("[MCP] Connected. Tools available:", ", ".join(tool_names))

            # Optional: ensure browser binaries exist (if tool is present)
            if "browser_install" in tool_names:
                # Only call if your environment needs it; safe to skip otherwise.
                pass

            collected_js_snippets: List[str] = []
            last_snapshot_text: str = ""

            for i, step in enumerate(scenario.steps, start=1):
                tool = step["tool"]
                args = step.get("args") or {}
                print(f"[MCP] Step {i}: {tool} {args}")

                result = await call_tool(session, tool, args)
                text = _mcp_text(result)

                # Keep snapshots around for ref-picking/debug
                if tool == "browser_snapshot":
                    last_snapshot_text = text
                    # Save snapshot to file for easy ref lookup
                    snap_dir = Path("reports/mcp_snapshots")
                    _ensure_dir(snap_dir)
                    (snap_dir / f"{slugify(scenario.test_name)}_step{i}.txt").write_text(text, encoding="utf-8")

                # Many Playwright MCP tool results include a "Ran Playwright code" code-block.
                # We extract those and convert to Python-ish sync calls.
                for block in _extract_code_blocks(text):
                    collected_js_snippets.append(block)

            # Convert collected JS snippets to Python sync-ish steps
            python_steps: List[str] = []
            for js in collected_js_snippets:
                python_steps.extend(js_to_python_sync(js))

            # Fallback: if nothing was emitted as code blocks, still create a skeleton.
            if not python_steps:
                python_steps = [
                    f'page.goto("{scenario.base_url}")',
                    "# TODO: Add steps. See reports/mcp_snapshots/*.txt for refs.",
                ]

            # Write generated test
            out_dir = Path("tests/generated")
            _ensure_dir(out_dir)
            out_file = out_dir / f"test_{slugify(scenario.test_name)}.py"
            out_file.write_text(render_pytest_test(scenario.test_name, scenario.base_url, python_steps), encoding="utf-8")

            print(f"[OK] Generated: {out_file}")
            print("[INFO] Snapshot refs (for click/type) saved under: reports/mcp_snapshots/")
            if last_snapshot_text:
                print("[TIP] Open the latest snapshot file and copy the exact `ref` strings into your scenario JSON.")
            return out_file

        finally:
            await session.aclose()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python tools/mcp_generate_test.py scenarios/<scenario>.json")
        sys.exit(2)

    scenario_path = Path(sys.argv[1]).resolve()
    if not scenario_path.exists():
        print(f"Scenario file not found: {scenario_path}")
        sys.exit(2)

    asyncio.run(run_generation(scenario_path))


if __name__ == "__main__":
    main()
