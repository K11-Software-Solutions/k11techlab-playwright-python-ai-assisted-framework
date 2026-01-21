import pytest
from playwright.sync_api import Page, expect
import os

@pytest.mark.advanced
def test_file_upload(page: Page, tmp_path):
    # Create a temporary file to upload
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Playwright file upload test.")

    page.goto("https://the-internet.herokuapp.com/upload")
    page.set_input_files("#file-upload", str(file_path))
    page.click("#file-submit")
    expect(page.locator("#uploaded-files")).to_have_text("sample.txt")
