import pytest
from tests.device_demo._demo_utils import save_screenshot

@pytest.mark.smoke
@pytest.mark.device
@pytest.mark.demo
@pytest.mark.parametrize("device_name", ["iPhone 12", "Pixel 5", "iPad (gen 7)"])
def test_device_emulation_matrix(browser, playwright, demo_artifacts_dir, device_name):
    device = playwright.devices[device_name]
    context = browser.new_context(**device)
    page = context.new_page()

    page.goto("https://example.com/")
    ua = page.evaluate("navigator.userAgent")

    save_screenshot(page, demo_artifacts_dir, f"device_{device_name.replace(' ', '_')}")
    assert isinstance(ua, str) and len(ua) > 10

    context.close()
