import pytest
from playwright.sync_api import Page, expect

@pytest.mark.playwright_example
@pytest.mark.no_base_url_navigation
def test_file_download(page: Page, tmp_path):
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.click(".example a")
    download = download_info.value
    download.save_as(tmp_path / download.suggested_filename)
    assert (tmp_path / download.suggested_filename).exists()
