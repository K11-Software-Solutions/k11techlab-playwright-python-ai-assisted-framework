import pytest
from playwright.sync_api import expect

@pytest.mark.advanced
def test_device_emulation(browser):
    # Emulate iPhone 12 by creating a new context
    iphone = {
        "viewport": {"width": 390, "height": 844},
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    }
    context = browser.new_context(viewport=iphone["viewport"], user_agent=iphone["user_agent"])
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    expect(page).to_have_title("Wikipedia")
    assert page.viewport_size["width"] == iphone["viewport"]["width"]
    context.close()
