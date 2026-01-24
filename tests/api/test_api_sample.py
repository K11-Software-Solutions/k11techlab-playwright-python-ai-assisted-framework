import pytest
from utilities.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient(base_url="https://jsonplaceholder.typicode.com")

def test_get_posts(api_client):
    response = api_client.get("/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post(api_client):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = api_client.post("/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"
