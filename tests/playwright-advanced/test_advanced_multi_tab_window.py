import pytest
from playwright.sync_api import Page, expect

@pytest.mark.advanced
def test_multi_tab_handling(page: Page, context):
    page.goto("https://the-internet.herokuapp.com/windows")
    with context.expect_page() as new_page_info:
        page.click("a[href='/windows/new']")
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://the-internet.herokuapp.com/windows/new")
    expect(new_page.locator("h3")).to_have_text("New Window")
    new_page.close()
    expect(page).to_have_url("https://the-internet.herokuapp.com/windows")
