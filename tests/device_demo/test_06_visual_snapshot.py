# Test 06: Visual Snapshot
import pytest
from tests.device_demo._demo_utils import save_screenshot

@pytest.mark.device
@pytest.mark.demo
def test_visual_snapshot(browser, playwright, demo_artifacts_dir):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.whatismybrowser.com/")
    path = save_screenshot(page, demo_artifacts_dir, "visual_snapshot")
    print(f"Screenshot saved to {path}")
    assert path.exists()
    context.close()
