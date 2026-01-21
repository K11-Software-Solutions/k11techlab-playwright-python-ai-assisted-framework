import pytest
from pages.contact_page import ContactPage

@pytest.fixture(scope="session")
def base_url(request):
	return request.config.getoption("base_url").rstrip("/")

@pytest.fixture
def contact_url(base_url):
	return f"{base_url}/contact"

@pytest.fixture
def contact_data():
	return {"name": "Test User", "email": "test@example.com", "message": "Hello!"}

def test_contact_sent_visible(page, contact_url, contact_data):
	contact = ContactPage(page)
	page.goto(contact_url)
	contact.send_message(contact_data["name"], contact_data["email"], contact_data["message"])
	assert contact.is_sent_visible()
# ...existing code...
