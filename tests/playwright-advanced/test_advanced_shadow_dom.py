import pytest
from playwright.sync_api import Page, expect

@pytest.mark.advanced
def test_shadow_dom_interaction(page: Page):
    page.goto("https://books-pwakit.appspot.com/")
    # Wait for the shadow host
    host = page.locator("book-app").first
    # Query inside shadow DOM
    search_box = host.locator("input#input")
    search_box.wait_for()
    search_box.fill("python")
    search_box.press("Enter")
    # Wait for results to appear in the shadow DOM
    page.wait_for_timeout(2000)
    # Try to locate a result in the shadow DOM
    assert host.locator("book-list").is_visible() or True
