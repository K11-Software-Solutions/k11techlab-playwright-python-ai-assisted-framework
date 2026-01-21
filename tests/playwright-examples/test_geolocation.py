import pytest
from playwright.sync_api import expect

@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
def test_geolocation(context):
    # Set geolocation and permissions on the context
    context.grant_permissions(["geolocation"], origin="https://www.openstreetmap.org")
    context.set_geolocation({"longitude": 12.4924, "latitude": 41.8902})
    page = context.new_page()
    page.goto("https://www.openstreetmap.org/")
    try:
        # Wait for the geolocate button to be visible before clicking
        page.locator(".icon-geolocate").wait_for(state="visible", timeout=10000)
        page.click(".icon-geolocate")
    except Exception as e:
        # Capture screenshot for diagnostics if the element is not found
        page.screenshot(path="reports/screenshots/geolocation_not_found.png")
        print("[DEBUG] .icon-geolocate not found or not visible. Screenshot saved.")
        raise
    expect(page.locator(".leaflet-popup-content")).to_contain_text("You are here")
    page.close()
