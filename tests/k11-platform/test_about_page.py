import pytest
from pages.about_page import AboutPage

@pytest.fixture(scope="session")
def base_url(request):
	return request.config.getoption("base_url").rstrip("/")

@pytest.fixture
def about_url(base_url):
	return f"{base_url}/about"

def test_about_page_loaded(page, about_url):
	about = AboutPage(page)
	page.goto(about_url)
	assert about.is_loaded()

def test_about_title(page, about_url):
	about = AboutPage(page)
	page.goto(about_url)
	assert about.get_title() is not None
