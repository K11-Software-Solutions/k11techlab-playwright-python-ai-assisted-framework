"""
Demo: Real Device Touch and Orientation
This test demonstrates touch and orientation on a real device profile.
"""
import pytest
from tests.device_demo._demo_utils import save_screenshot

@pytest.mark.device
@pytest.mark.realdevice
def test_real_device_touch_orientation(browser, playwright, demo_artifacts_dir):
    device = playwright.devices["Pixel 5"]
    valid_keys = {k: v for k, v in device.items() if k not in ["default_browser_type", "name"]}
    context = browser.new_context(**valid_keys)
    page = context.new_page()
    page.goto("https://www.google.com/doodles")
    # Simulate tap on the first doodle (if present)
    doodle = page.locator("a.doodle-card").first
    if doodle.count() > 0:
        doodle.click()
    save_screenshot(page, demo_artifacts_dir, "real_device_touch_orientation")
    context.close()
