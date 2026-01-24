from __future__ import annotations
from pathlib import Path

def save_screenshot(page, out_dir: Path, name: str) -> Path:
    path = out_dir / f"{name}.png"
    page.screenshot(path=str(path), full_page=True)
    return path

def start_trace(context, out_dir: Path, name: str) -> None:
    # Optional: enable if you want trace files in demos
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

def stop_trace(context, out_dir: Path, name: str) -> None:
    path = out_dir / f"{name}.zip"
    context.tracing.stop(path=str(path))
