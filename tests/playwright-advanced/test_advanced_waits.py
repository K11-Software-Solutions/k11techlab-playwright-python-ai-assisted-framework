import pytest
from playwright.sync_api import Page, expect

@pytest.mark.advanced
def test_explicit_wait_for_element(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")
    page.wait_for_selector(".new-todo")
    expect(page.locator(".new-todo")).to_be_visible()

@pytest.mark.advanced
def test_wait_for_network_idle(page: Page):
    page.goto("https://demo.playwright.dev/todomvc")
    page.wait_for_load_state("networkidle")
    expect(page.locator(".todoapp")).to_be_visible()
