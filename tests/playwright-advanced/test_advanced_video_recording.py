import pytest
from playwright.sync_api import expect
import os

@pytest.mark.advanced
def test_video_recording(browser, tmp_path):
    video_dir = tmp_path / "videos"
    video_dir.mkdir()
    context = browser.new_context(record_video_dir=str(video_dir))
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    page.click("a[href='/login']")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    video_path = page.video.path()
    context.close()
    assert os.path.exists(video_path)
