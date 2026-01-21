# AI-Assisted Self-Healing Locator Utility
# See doc/ai_self_healing_locators.md for usage and extension points

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from typing import List, Optional, Callable
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Example: Local Ollama (REST API)
def ollama_ai_model(selector: str, alternatives: List[str]) -> str:
    """
    Suggest a new selector using a local Ollama model via REST API.
    Requires OLLAMA_BASE_URL and OLLAMA_MODEL_NAME in .env.
    """
    import requests
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model_name = os.getenv("OLLAMA_MODEL_NAME", "llama2")
    prompt = f"Suggest a robust Playwright selector for: {selector}. Alternatives: {alternatives}"
    try:
        response = requests.post(
            f"{base_url}/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": 32}
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except Exception:
        return None

# Example: Local LLM (llama-cpp-python)
def local_llm_ai_model(selector: str, alternatives: List[str]) -> str:
    """
    Suggest a new selector using a local LLM (e.g., llama-cpp-python).
    Requires LLAMA_MODEL_PATH in .env.
    """
    try:
        from llama_cpp import Llama
        model_path = os.getenv("LLAMA_MODEL_PATH")
        if not model_path:
            return None
        llm = Llama(model_path=model_path)
        prompt = f"Suggest a robust selector for: {selector}. Alternatives: {alternatives}"
        output = llm(prompt, max_tokens=32)
        # Parse output for selector (customize as needed)
        return output["choices"][0]["text"].strip()
    except Exception:
        return None

# Example: OpenAI GPT-3/4
def openai_ai_model(selector: str, alternatives: List[str]) -> str:
    """
    Suggest a new selector using OpenAI API. Requires OPENAI_API_KEY in .env.
    """
    import openai
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    openai.api_key = api_key
    prompt = f"Suggest a robust Playwright selector for: {selector}. Alternatives: {alternatives}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=32
        )
        return response.choices[0].text.strip()
    except Exception:
        return None

# Example: Anthropic Claude
def anthropic_ai_model(selector: str, alternatives: List[str]) -> str:
    """
    Suggest a new selector using Anthropic Claude API. Requires ANTHROPIC_API_KEY in .env.
    """
    import anthropic
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    client = anthropic.Anthropic(api_key=api_key)
    prompt = f"Suggest a robust Playwright selector for: {selector}. Alternatives: {alternatives}"
    try:
        response = client.completions.create(
            model="claude-2",
            prompt=prompt,
            max_tokens_to_sample=32
        )
        return response.completion.strip()
    except Exception:
        return None

# Utility to select AI model backend
def get_ai_model(backend: str) -> Callable[[str, List[str]], Optional[str]]:
    """
    Returns the appropriate AI model function based on backend string.
    backend: 'local', 'ollama', 'openai', or 'anthropic'
    """
    if backend == "local":
        return local_llm_ai_model
    elif backend == "ollama":
        return ollama_ai_model
    elif backend == "openai":
        return openai_ai_model
    elif backend == "anthropic":
        return anthropic_ai_model
    else:
        return None


def find_element_with_self_healing(
    page: 'Page',
    selector: str,
    alternatives: Optional[List[str]] = None,
    ai_model: Optional[Callable[[str, List[str]], str]] = None,
    timeout: int = 3000
):
    """
    Attempts to find an element using the original selector.
    If it fails, tries alternatives and/or uses an AI/ML model to suggest a fix.
    Returns the element handle if found, else raises the last exception.

    Parameters:
        page: Playwright Page object.
        selector: The primary selector string for the element.
        alternatives: List of backup selectors to try if the primary fails. These can be CSS, text, role, or XPath selectors.
            Example: ["button[type='submit']", "text=Submit", "button.btn-primary"]
        ai_model: (Optional) Callable that takes the original selector and alternatives, and returns a new selector (e.g., from an LLM or ML model).
            Example:
                def my_ai_model(selector, alternatives):
                    # Use LLM or ML to suggest a new selector
                    return "text=AI Suggested Selector"
        timeout: Timeout in milliseconds for each selector attempt.
    """
    # If no alternatives provided, use an empty list
    alternatives = alternatives or []
    try:
        return page.locator(selector).first.wait_for(state="attached", timeout=timeout)
    except PlaywrightTimeoutError:
        pass

    # Try alternatives
    for alt in alternatives:
        try:
            return page.locator(alt).first.wait_for(state="attached", timeout=timeout)
        except PlaywrightTimeoutError:
            continue

    # Optionally, use AI/ML model to suggest a new selector
    if ai_model:
        ai_selector = ai_model(selector, alternatives)
        if ai_selector:
            try:
                return page.locator(ai_selector).first.wait_for(state="attached", timeout=timeout)
            except PlaywrightTimeoutError:
                pass

    raise PlaywrightTimeoutError(f"Element not found: {selector} (tried {alternatives})")
