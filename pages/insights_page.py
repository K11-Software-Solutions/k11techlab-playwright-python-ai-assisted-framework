

from playwright.sync_api import Page

class InsightsPage:
    """Page Object Model for the Insights page, using element IDs from the prompt."""
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#insights-container')
        # Add a locator for all links inside the insights container
        self.links = self.container.locator('a')

    def is_loaded(self):
        return self.container.is_visible()

    def get_all_links(self):
        """Return a list of hrefs for all links in the insights container."""
        return self.links.evaluate_all("elements => elements.map(el => el.href)")
