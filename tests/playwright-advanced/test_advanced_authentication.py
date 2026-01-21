import pytest
from playwright.sync_api import Page, expect

@pytest.mark.advanced
def test_http_basic_auth(context, page: Page):
    # Use context with http_credentials for basic auth
    # This test assumes pytest-playwright context fixture is available
    # If not, create a new context with http_credentials
    creds = {"username": "admin", "password": "admin"}
    with context.new_page() as auth_page:
        auth_page.context.set_extra_http_headers({
            "Authorization": "Basic YWRtaW46YWRtaW4="  # base64 for admin:admin
        })
        auth_page.goto("https://the-internet.herokuapp.com/basic_auth")
        expect(auth_page.locator(".example p")).to_have_text("Congratulations! You must have the proper credentials.")
