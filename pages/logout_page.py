# logout_page.py
# =====================
# This class represents the "Logout Page" of the application.
# It follows the Page Object Model (POM) design pattern
# to separate page locators and actions from the test logic.

from playwright.sync_api import Page, expect
from pages.home_page import HomePage  # Adjust this import path as per your project structure


class LogoutPage:
    """Page Object Model class for the Logout Page."""

    def __init__(self, page: Page):
        """
        Constructor that initializes the Playwright Page instance
        and defines all locators used on the Logout Page.
        """
        self.page = page

        # ===== Locators =====
        # Button used to return to the home page after successful logout
        self.btn_continue = page.locator('.btn.btn-primary')

    # ===== Action Methods =====

    def click_continue(self):
        """
        Click the 'Continue' button after logging out.
        This typically redirects the user back to the Home Page.
        """
        try:
            self.btn_continue.click()
        except Exception as e:
            print(f" Exception while clicking 'Continue' button: {e}")
            raise

    def get_continue_button(self):
        """
        Return the Continue button locator.
        Useful for checking its visibility or state in test assertions.

        Example:
            expect(logout_page.get_continue_button()).to_be_visible()
        """
        try:
            return self.btn_continue
        except Exception as e:
            print(f" Exception while fetching 'Continue' button locator: {e}")
            return None
