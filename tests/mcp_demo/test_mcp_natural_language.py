"""
Demo: Playwright MCP (Model Context Protocol) - Natural Language Test Generation
This test demonstrates how to use Azure OpenAI to generate Playwright tests from natural language instructions.
Includes safety checks and logs generated code to a file.
"""
import pytest
from playwright.sync_api import sync_playwright
import openai
import os
import re

# List of natural language prompts for demo
prompts = [
    "Test that the Wikipedia homepage loads and the search box is visible.",
    "Verify that the GitHub login page loads and the username field is present.",
    "Check that the Python.org homepage loads and the Downloads link is visible.",
]

def mcp_generate_code(prompt, openai_api_key):
    # openai v1+ API usage
    client = openai.OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that writes Playwright Python tests."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def is_code_safe(code):
    # Basic safety: block dangerous builtins and OS/system calls
    forbidden = [r'os\.', r'sys\.', r'open\(', r'eval\(', r'exec\(', r'subprocess', r'__import__', r'input\(', r'globals\(', r'locals\(']
    for pattern in forbidden:
        if re.search(pattern, code):
            return False
    return True

def log_generated_code(prompt, code):
    with open("generated_mcp_code.log", "a", encoding="utf-8") as f:
        f.write(f"\nPROMPT: {prompt}\nCODE:\n{code}\n{'-'*40}\n")

@pytest.mark.mcp_demo
@pytest.mark.parametrize("prompt", prompts)
def test_mcp_generate_and_run(prompt):
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        pytest.skip("OPENAI_API_KEY environment variable not set.")
    # Generate Playwright test code from natural language prompt
    code = mcp_generate_code(prompt, openai_api_key)
    print("\nGenerated code:\n", code)
    log_generated_code(prompt, code)
    if not is_code_safe(code):
        pytest.skip("Generated code failed safety checks and was not executed.")
    # WARNING: Only exec() trusted code in a safe environment!
    # For demo, we run the generated code in a local namespace
    local_vars = {}
    exec(code, globals(), local_vars)

# To use: set your OpenAI API key in the environment variable OPENAI_API_KEY
# export OPENAI_API_KEY=sk-...
