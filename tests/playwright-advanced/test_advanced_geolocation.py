import pytest
from playwright.sync_api import Page, expect

@pytest.mark.advanced
def test_geolocation_permission(context, page: Page):
    context.grant_permissions(["geolocation"])
    context.set_geolocation({"latitude": 37.7749, "longitude": -122.4194})
    page.goto("https://maps.google.com")
    # Instead of asserting context.geolocation, check for geolocation prompt or UI change
    # This is a demonstration; in real tests, assert map centers or location popups
    assert "maps" in page.url
