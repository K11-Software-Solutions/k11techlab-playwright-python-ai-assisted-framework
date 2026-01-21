import pytest
from playwright.sync_api import Page, expect
import os

@pytest.mark.advanced
def test_file_download(page: Page, tmp_path):
    page.goto("https://the-internet.herokuapp.com/download")
    # Wait for at least one download link to be visible
    page.wait_for_selector("#content a")
    with page.expect_download() as download_info:
        page.click("#content a")
    download = download_info.value
    download_path = tmp_path / download.suggested_filename
    download.save_as(str(download_path))
    assert download_path.exists()
    assert download_path.stat().st_size > 0
