import pytest
from playwright.sync_api import Page, expect

@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
def test_network_mocking(page: Page):
    def handle_route(route):
        route.fulfill(
            status=200,
            body="<html><body><h1>Mocked Response!</h1></body></html>",
            content_type="text/html"
        )
    page.route("**/mocked-url", handle_route)
    page.goto("https://the-internet.herokuapp.com")
    page.evaluate('''fetch("/mocked-url").then(r => r.text()).then(t => document.body.innerHTML = t)''')
    expect(page.locator("h1")).to_have_text("Mocked Response!")
