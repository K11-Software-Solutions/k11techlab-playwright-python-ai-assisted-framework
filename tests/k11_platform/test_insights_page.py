import pytest
from pages.k11_platform.insights_page import InsightsPage

@pytest.fixture(scope="session")
def base_url(request):
	return request.config.getoption("base_url").rstrip("/")

@pytest.fixture
def insights_url(base_url):
	return f"{base_url}/insights"

def test_insights_page_loaded(page, insights_url):
	insights = InsightsPage(page)
	page.goto(insights_url)
	assert insights.is_loaded()
# ...existing code...
