import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.real_device
def test_real_android_chrome():
    with sync_playwright() as p:
        # Attach to real Android Chrome via CDP
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.whatismybrowser.com/")
        ua = page.evaluate("navigator.userAgent")
        assert "Android" in ua or "Linux; Android" in ua
        context.close()
        browser.close()
