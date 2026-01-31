"""
Demo: Real iOS Safari Testing via BrowserStack (Cloud)
This is a sample Playwright test for running on real iOS devices in BrowserStack cloud.
See doc/real_devices.md for setup and credentials.
"""
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.real_device
def test_real_ios_safari_browserstack():
    # This is a template. You must set up BrowserStack credentials and capabilities.
    # See https://www.browserstack.com/docs/automate/playwright/ios for details.
    capabilities = {
        "browser": "ios",
        "device": "iPhone 14",
        "os_version": "16",
        "real_mobile": True,
        "name": "Playwright iOS Safari Test",
        "build": "playwright-ios-demo"
    }
    # Example: connect to BrowserStack (requires playwright.config or CLI setup)
    # with sync_playwright() as p:
    #     browser = p.webkit.connect_over_cdp("wss://cdp.browserstack.com/playwright?caps=...", headers={...})
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto("https://www.whatismybrowser.com/")
    #     assert "iPhone" in page.title() or "Safari" in page.title()
    #     context.close()
    #     browser.close()
    pass  # See doc/real_devices.md for full instructions
