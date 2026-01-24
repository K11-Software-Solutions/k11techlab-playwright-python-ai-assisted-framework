import pytest
from pages.k11_platform.home_page import HomePage

@pytest.fixture(scope="session")
def base_url(request):
	return request.config.getoption("base_url").rstrip("/")

@pytest.fixture
def home_url(base_url):
	return f"{base_url}/"

@pytest.mark.smoke
@pytest.mark.ui
def test_home_hero_section_visible(page, home_url):
	home = HomePage(page)
	page.goto(home_url)
	assert home.is_hero_section_visible()

@pytest.mark.regression
@pytest.mark.ui
def test_home_hero_title(page, home_url):
	home = HomePage(page)
	page.goto(home_url)
	assert home.get_hero_title() is not None
# ...existing code...
