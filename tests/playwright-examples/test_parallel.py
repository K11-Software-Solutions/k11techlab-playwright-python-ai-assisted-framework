import pytest
from playwright.sync_api import Page, expect

@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
@pytest.mark.parametrize(
    "url,test_id,title",
    [
        ("https://demo.playwright.dev/todomvc", "todomvc", "React • TodoMVC"),
        ("https://the-internet.herokuapp.com", "the_internet", "The Internet"),
    ],
    ids=["todomvc", "the_internet"]
)
def test_parallel_navigation(page: Page, url, test_id, title):
    page.goto(url)
    expect(page).to_have_title(title)
