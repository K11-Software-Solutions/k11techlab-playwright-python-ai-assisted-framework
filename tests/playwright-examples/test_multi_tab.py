import pytest
from playwright.sync_api import Page, expect

@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
def test_multi_tab_handling(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows")
    page.click("a[href='/windows/new']")
    new_page = page.context.wait_for_event("page")
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://the-internet.herokuapp.com/windows/new")
    expect(new_page.locator("h3")).to_have_text("New Window")
