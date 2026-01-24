import pytest
from tests.device_demo._demo_utils import save_screenshot

HTML = """
<!doctype html>
<html>
<body style="font-family:system-ui;padding:18px;">
  <h2>Locale/Timezone/Dark + Network Demo</h2>
  <pre id="info"></pre>
  <pre id="api"></pre>
  <script>
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const lang = navigator.language;
    const dark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    info.textContent = JSON.stringify({ tz, lang, dark }, null, 2);

    fetch(window.location.origin + "/api/data")
      .then(r => r.json())
      .then(j => api.textContent = "API: " + JSON.stringify(j))
      .catch(e => api.textContent = "API ERROR: " + e.toString());
  </script>
</body>
</html>
"""

@pytest.mark.demo
def test_locale_timezone_darkmode_and_network(browser, demo_artifacts_dir):
    context = browser.new_context(
      locale="en-GB",
      timezone_id="Europe/London",
      color_scheme="dark"
    )
    # Mock fetch for /api/data before any scripts run
    context.add_init_script(
      """
      const originalFetch = window.fetch;
      window.fetch = function(url, ...args) {
        if (typeof url === 'string' && url.includes('/api/data')) {
          return Promise.resolve({
            json: () => Promise.resolve({status: 'ok', source: 'mock'})
          });
        }
        return originalFetch.apply(this, [url, ...args]);
      };
      """
    )
    page = context.new_page()
    page.set_content(HTML)
    info = page.locator("#info").inner_text()
    api = page.locator("#api").inner_text()

    save_screenshot(page, demo_artifacts_dir, "locale_tz_dark_network")
    assert "Europe/London" in info
    assert "en-GB" in info
    assert '"dark": true' in info
    assert "API: " in api
    assert '"status":"ok"' in api

    context.close()
