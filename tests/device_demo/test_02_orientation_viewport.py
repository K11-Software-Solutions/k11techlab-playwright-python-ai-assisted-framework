import pytest
from tests.device_demo._demo_utils import save_screenshot

@pytest.mark.device
@pytest.mark.demo
def test_orientation_viewport_override(browser, playwright, demo_artifacts_dir):
    device = playwright.devices["iPhone 12"]

    # Portrait (device default)
    ctx_portrait = browser.new_context(**device)
    page_p = ctx_portrait.new_page()
    page_p.set_content("<h1>Portrait</h1>")
    vp_p = page_p.viewport_size
    save_screenshot(page_p, demo_artifacts_dir, "orientation_portrait")
    assert vp_p["height"] > vp_p["width"]
    ctx_portrait.close()

    # Landscape (swap viewport)
    device_no_viewport = {k: v for k, v in device.items() if k != "viewport"}
    vp = device.get("viewport", {"width": 390, "height": 844})
    ctx_landscape = browser.new_context(**device_no_viewport, viewport={"width": vp["height"], "height": vp["width"]})
    page_l = ctx_landscape.new_page()
    page_l.set_content("<h1>Landscape</h1>")
    vp_l = page_l.viewport_size
    save_screenshot(page_l, demo_artifacts_dir, "orientation_landscape")
    assert vp_l["width"] > vp_l["height"]
    ctx_landscape.close()
