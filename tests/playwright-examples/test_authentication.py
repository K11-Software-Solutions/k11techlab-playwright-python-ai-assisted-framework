import pytest
from playwright.sync_api import Page, expect

@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
def test_http_authentication(page: Page):
    # Recreate context with http_credentials for basic auth
    context = page.context
    context.close()
    new_context = context.browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    new_page = new_context.new_page()
    new_page.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(new_page.locator(".example p")).to_contain_text("Congratulations!")
    new_context.close()
