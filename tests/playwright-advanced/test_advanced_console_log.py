import pytest
from playwright.sync_api import Page

@pytest.mark.advanced
def test_capture_console_logs(page: Page):
    logs = []
    def on_console(msg):
        logs.append(msg.text)
    page.on("console", on_console)
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.evaluate("console.log('Playwright log test')")
    assert any("Playwright log test" in log for log in logs)
