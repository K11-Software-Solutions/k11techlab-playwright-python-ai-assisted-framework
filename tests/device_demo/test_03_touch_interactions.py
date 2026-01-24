
import pytest
import pathlib
from tests.device_demo._demo_utils import save_screenshot

HTML = """
<!doctype html>
<html>
  <body style="font-family: system-ui; padding: 20px;">
    <h2>Touch Demo</h2>
    <button id="tap" style="padding:12px 16px; font-size:16px;">Tap me</button>
    <p id="status">waiting</p>

    <div style="margin-top:20px;">
      <div id="box" style="width:120px;height:60px;border-radius:12px;background:#2ddc7d;
                           display:flex;align-items:center;justify-content:center;color:#062b1a;">
        drag
      </div>
      <div id="drop" style="margin-top:16px;width:240px;height:90px;border:2px dashed #ffffff55;
                            border-radius:14px;display:flex;align-items:center;justify-content:center;">
        drop zone
      </div>
      <p id="dropStatus">not dropped</p>
    </div>

    <script>
      tap.addEventListener("click", () => status.textContent = "tapped");
      box.addEventListener("dragstart", e => e.dataTransfer.setData("text/plain", "ok"));
      drop.addEventListener("dragover", e => e.preventDefault());
      drop.addEventListener("drop", e => { e.preventDefault(); dropStatus.textContent = "dropped"; });
      box.setAttribute("draggable", "true");
    </script>
  </body>
</html>
"""

@pytest.mark.device
@pytest.mark.demo
def test_touch_tap_and_drag(browser, playwright, demo_artifacts_dir):
    device = playwright.devices["Pixel 5"]
    # Remove keys not accepted by new_context (like 'default_browser_type', 'name')
    valid_keys = {
      k: v for k, v in device.items()
      if k in [
        "user_agent", "viewport", "device_scale_factor", "is_mobile", "has_touch",
        "screen", "permissions", "color_scheme", "reduced_motion", "timezone_id", "locale"
      ]
    }
    context = browser.new_context(**valid_keys)
    page = context.new_page()

    import http.server
    import socketserver
    import threading
    import time

    # Serve the directory containing the HTML file
    html_dir = pathlib.Path(__file__).parent
    PORT = 8765
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(0.5)  # Give server time to start

    try:
      page.goto(f"http://localhost:{PORT}/touch_demo.html")
      page.locator("#tap").tap()
      assert page.locator("#status").inner_text() == "tapped"

      page.drag_and_drop("#box", "#drop")
      assert page.locator("#dropStatus").inner_text() == "dropped"

      save_screenshot(page, demo_artifacts_dir, "touch_tap_drag")
    finally:
      httpd.shutdown()
      server_thread.join()
    context.close()
    # Use Playwright's click to simulate a real user gesture
    page.locator("#tap").click()
    assert page.locator("#status").inner_text() == "tapped"

    page.drag_and_drop("#box", "#drop")
    assert page.locator("#dropStatus").inner_text() == "dropped"

    save_screenshot(page, demo_artifacts_dir, "touch_tap_drag")
    context.close()
