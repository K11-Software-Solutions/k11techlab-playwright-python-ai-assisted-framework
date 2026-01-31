"""
Demo: Real Device Geolocation Permissions
This test demonstrates geolocation and permissions on a real device profile.
"""
import pytest
from tests.device_demo._demo_utils import save_screenshot

@pytest.mark.device
@pytest.mark.realdevice
def test_real_device_geolocation(browser, playwright, demo_artifacts_dir):
    device = playwright.devices["iPhone 12"]
    valid_keys = {k: v for k, v in device.items() if k not in ["default_browser_type", "name"]}
    context = browser.new_context(
        **valid_keys,
        geolocation={"longitude": 12.4924, "latitude": 41.8902},  # Rome
        permissions=["geolocation"]
    )
    page = context.new_page()
    page.goto("https://maps.google.com")
    save_screenshot(page, demo_artifacts_dir, "real_device_geolocation")
    # No assertion: visual/manual check for location prompt
    context.close()
