import pytest
from playwright.sync_api import Page, expect

@pytest.mark.advanced
def test_handle_js_alert(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())
    page.click("button[onclick='jsAlert()']")
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

@pytest.mark.advanced
def test_handle_js_confirm(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.click("button[onclick='jsConfirm()']")
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")
