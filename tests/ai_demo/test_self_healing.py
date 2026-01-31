import pytest
from ai.self_healing import find_element_with_self_healing, get_ai_model


@pytest.mark.ai
def test_basic_navigation_and_services_link(page):
    """
    Test basic navigation to k11softwaresolutions.com and clicking on the Services link using robust selectors and AI fallback.
    """
    page.goto("https://k11softwaresolutions.com")
    # Try robust selectors for Explore Services button
    selectors = [
        "button:has-text('Explore services')",
        "button:has-text('explore services')",
        "a:has-text('Explore services')",
        "a:has-text('explore services')",
        "[role='button']:has-text('Explore services')",
        "[role='button']:has-text('explore services')",
        "[class*='explore-services']",
        "[data-testid*='explore-services']"
    ]
    found = False
    for sel in selectors:
        try:
            btn = page.locator(sel)
            btn.wait_for(state="visible", timeout=3000)
            btn.hover()
            btn.click()
            found = True
            print(f"[DEBUG] Hovered and clicked Explore Services button with selector: {sel}")
            break
        except Exception:
            continue
    if not found:
        print("[DEBUG] All robust selectors failed. Trying AI self-healing.")
        ai_model = get_ai_model("ollama")  # or "openai", "local", etc.
        elem = find_element_with_self_healing(
            page,
            selector=selectors[0],
            alternatives=selectors[1:],
            ai_model=ai_model,
            timeout=2000
        )
        if elem is None:
            ai_suggestion = ai_model(selectors[0], selectors[1:]) if ai_model else None
            print(f"[DEBUG] AI suggestion: {ai_suggestion}")
            page.screenshot(path="reports/screenshots/explore_services_not_found.png")
            print("[DEBUG] All selectors failed. Screenshot saved to reports/screenshots/explore_services_not_found.png")
        assert elem is not None, "Explore Services button not found by any selector or AI suggestion. See screenshot and logs."
        page.hover(elem.selector)
        page.click(elem.selector)
    # Optionally, validate navigation to Services page
    from playwright.sync_api import expect
    expect(page).to_have_url(lambda url: "services" in url)
    page.close()
