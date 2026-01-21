import pytest
from pages.register_page import RegisterPage


@pytest.fixture
def registration_data():
	# Replace with secure retrieval or parameterization as needed
	return {"username": "user1", "email": "user1@example.com", "password": "password123", "subscription": "basic"}


@pytest.fixture(scope="session")
def base_url(request):
	return request.config.getoption("base_url").rstrip("/")


@pytest.fixture
def register_url(base_url):
	return f"{base_url}/register"

def test_register_success_visible(page, registration_data, register_url):
	register = RegisterPage(page)
	page.goto(register_url)
	register.register(
		registration_data["username"],
		registration_data["email"],
		registration_data["password"],
		registration_data["subscription"]
	)
	assert register.is_success_visible()
# ...existing code...
