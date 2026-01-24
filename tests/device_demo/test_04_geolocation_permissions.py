import pytest
from tests.device_demo._demo_utils import save_screenshot

@pytest.mark.device
@pytest.mark.demo
def test_geolocation_permission_flow(browser, playwright, demo_artifacts_dir):
    lat, lon = 51.5072, -0.1276  # London (demo)

    device = playwright.devices["iPhone 12"]
    context = browser.new_context(
        **device,
        geolocation={"latitude": lat, "longitude": lon},
        permissions=["geolocation"],
    )
    page = context.new_page()
    page.goto("https://example.com/")

    coords = page.evaluate("""
      () => new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
          p => resolve({lat: p.coords.latitude, lon: p.coords.longitude}),
          e => reject(e.message)
        );
      })
    """)

    save_screenshot(page, demo_artifacts_dir, "geo_example_com")
    assert abs(coords["lat"] - lat) < 1.0
    assert abs(coords["lon"] - lon) < 1.0

    context.close()
