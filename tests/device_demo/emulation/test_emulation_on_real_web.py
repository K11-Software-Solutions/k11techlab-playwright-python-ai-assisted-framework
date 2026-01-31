"""
Demo: Device Emulation with Playwright (using real web URLs)
This test demonstrates device emulation for various devices on a real website.
"""
import pytest
from tests.device_demo._demo_utils import save_screenshot

device_names = [
    "iPhone 12",
    "Pixel 5",
    "iPad (gen 7)"
]

@pytest.mark.device
@pytest.mark.emulation
@pytest.mark.parametrize("device_name", device_names)
def test_emulation_on_real_web(browser, playwright, device_name, demo_artifacts_dir):
    device = playwright.devices[device_name]
    valid_keys = {k: v for k, v in device.items() if k not in ["default_browser_type", "name"]}
    context = browser.new_context(**valid_keys)
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    save_screenshot(page, demo_artifacts_dir, f"emulation_{device_name.replace(' ', '_')}")
    assert "Wikipedia" in page.title()
    context.close()
