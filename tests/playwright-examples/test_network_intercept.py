import pytest
from playwright.sync_api import Page, expect

@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
def test_network_intercept(page: Page):
    def handle_route(route):
        if "logo" in route.request.url:
            route.abort()
        else:
            route.continue_()
    page.route("**/*", handle_route)
    page.goto("https://the-internet.herokuapp.com")
    # Logo should not be loaded
    expect(page.locator("img[src*='logo']")).to_have_count(0)
