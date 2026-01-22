from playwright.sync_api import Page

class AboutPage:
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#about-container')
        self.title = page.locator('#about-title')

    def is_loaded(self):
        return self.container.is_visible()

    def get_title(self):
        return self.title.text_content()
