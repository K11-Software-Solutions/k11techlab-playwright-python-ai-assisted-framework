import pytest
from playwright.sync_api import Page, expect

# Basic navigation and assertion example using Playwright's official demo site
@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
def test_basic_navigation(page: Page):
    page.goto("https://demo.playwright.dev/todomvc", timeout=10000)
    expect(page).to_have_title("React • TodoMVC", timeout=10000)
    expect(page.locator(".new-todo")).to_be_visible(timeout=10000)
    # Add a todo item
    page.fill(".new-todo", "Learn Playwright")
    page.keyboard.press("Enter")
    expect(page.locator(".todo-list li")).to_have_count(1, timeout=10000)
    expect(page.locator(".todo-list li label")).to_have_text(["Learn Playwright"], timeout=10000)
    # Mark as completed
    page.locator(".toggle").click()
    expect(page.locator(".todo-list li.completed")).to_have_count(1, timeout=10000)
    # Clear completed
    page.click(".clear-completed")
    expect(page.locator(".todo-list li")).to_have_count(0, timeout=10000)
