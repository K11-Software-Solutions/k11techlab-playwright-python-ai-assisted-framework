import pytest
from playwright.sync_api import Page

@pytest.mark.advanced
def test_network_request_interception(page: Page):
    intercepted = {}

    def handle_route(route, request):
        if "todomvc" in request.url:
            intercepted["called"] = True
        route.continue_()

    page.route("**/*", handle_route)
    page.goto("https://demo.playwright.dev/todomvc")
    assert intercepted.get("called"), "Network interception did not trigger."
