from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#dashboard-container')
        self.title = page.locator('#dashboard-title')
        self.welcome = page.locator('#dashboard-welcome')
        self.email = page.locator('#dashboard-email')
        self.logout = page.locator('#dashboard-logout')

    def is_loaded(self):
        return self.container.is_visible()

    def get_title(self):
        return self.title.text_content()

    def click_logout(self):
        self.logout.click()
