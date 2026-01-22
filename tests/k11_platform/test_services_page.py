import pytest
from pages.k11_platform.service_page import ServicePage



@pytest.fixture(scope="session")
def base_url(request):
	return request.config.getoption("base_url").rstrip("/")


@pytest.fixture
def services_url(base_url):
	return f"{base_url}/services"

def test_services_page_loaded(page, services_url):
	services = ServicePage(page)
	page.goto(services_url)
	assert services.is_loaded()

def test_services_title(page, services_url):
	services = ServicePage(page)
	page.goto(services_url)
	assert services.get_title() is not None
# ...existing code...
