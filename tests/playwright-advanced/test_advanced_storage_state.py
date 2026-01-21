import pytest
from playwright.sync_api import expect
import json

@pytest.mark.advanced
def test_storage_state_login(context, page, tmp_path):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    storage = context.storage_state()
    storage_path = tmp_path / "storage.json"
    with open(storage_path, "w") as f:
        json.dump(storage, f)
    assert storage_path.exists()
