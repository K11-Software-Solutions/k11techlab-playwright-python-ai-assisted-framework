
from playwright.sync_api import Page
from ai.self_healing import find_element_with_self_healing


class ServicePage:
    """
    Page Object Model for the Service Page (subscription service).
    Locators are based on provided element IDs from the frontend/app/services/page.js mapping.
    """
    def __init__(self, page: Page):
        self.page = page
        # Primary selectors
        self.container_selector = '#services-container'
        self.title_selector = '#services-title'
        self.service_items_selector = 'a, .service-item'
        # Alternatives for self-healing (extend as needed)
        self.container_alternatives = [
            "div.services-container",
            "section#services",
            "text=Services",
            "text=Our Services"
        ]
        self.title_alternatives = [
            "h1.services-title",
            "div#services-title",
            "text=Services",
            "text=Our Services"
        ]
        self.service_items_alternatives = [
            ".service-link",
            "li.service-item",
            "text=Subscribe",
            "text=Start Free Trial"
        ]


    def is_loaded(self) -> bool:
        """Check if the service page container is visible (self-healing)."""
        try:
            find_element_with_self_healing(
                self.page,
                self.container_selector,
                alternatives=self.container_alternatives
            )
            return True
        except Exception:
            return False


    def get_title(self) -> str:
        """Get the title text of the service page (self-healing)."""
        elem = find_element_with_self_healing(
            self.page,
            self.title_selector,
            alternatives=self.title_alternatives
        )
        return self.page.locator(self.title_selector).text_content()


    def title_is_visible(self) -> bool:
        """Check if the service page title is visible (self-healing)."""
        try:
            find_element_with_self_healing(
                self.page,
                self.title_selector,
                alternatives=self.title_alternatives
            )
            return True
        except Exception:
            return False


    def get_services_list(self):
        """Return a list of service names (text) from the services container (self-healing)."""
        # Ensure container is present (self-healing)
        find_element_with_self_healing(
            self.page,
            self.container_selector,
            alternatives=self.container_alternatives
        )
        # Try to get service items using self-healing
        try:
            find_element_with_self_healing(
                self.page,
                self.service_items_selector,
                alternatives=self.service_items_alternatives
            )
            return self.page.locator(self.service_items_selector).evaluate_all(
                "elements => elements.map(el => el.textContent.trim())"
            )
        except Exception:
            return []

