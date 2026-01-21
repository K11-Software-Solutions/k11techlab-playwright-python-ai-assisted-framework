import pytest
from playwright.sync_api import Page, expect

@pytest.mark.advanced
def test_request_mocking(page: Page):
    def handle_route(route, request):
        if "api" in request.url:
            route.fulfill(status=200, body='{"mocked": true}', content_type="application/json")
        else:
            route.continue_()
    page.route("**/api/**", handle_route)
    page.goto("https://example.com")
    # This is a demonstration; in real tests, assert on network or UI changes
    # Example: expect(page.locator("#api-result")).to_have_text("mocked")
    assert True
