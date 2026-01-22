import pytest
from pages.k11_platform.login_page import LoginPage

@pytest.fixture
def login_credentials():
	# Replace with secure retrieval or parameterization as needed
	return {"username": "invaliduser", "password": "invalidpass"}


@pytest.fixture(scope="session")
def base_url(request):
	return request.config.getoption("base_url").rstrip("/")


@pytest.fixture
def login_url(base_url):
	return f"{base_url}/login"

def test_login_error_visible(page, login_credentials, login_url):
	login = LoginPage(page)
	page.goto(login_url)
	login.login(login_credentials["username"], login_credentials["password"])
	assert login.is_error_visible()
# ...existing code...
