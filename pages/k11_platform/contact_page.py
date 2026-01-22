from playwright.sync_api import Page

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#contact-container')
        self.title = page.locator('#contact-title')
        self.form = page.locator('#contact-form')
        self.name = page.locator('#contact-name')
        self.email = page.locator('#contact-email')
        self.message = page.locator('#contact-message')
        self.submit = page.locator('#contact-submit')
        self.sent = page.locator('#contact-sent')

    def send_message(self, name, email, msg):
        self.name.fill(name)
        self.email.fill(email)
        self.message.fill(msg)
        self.submit.click()

    def is_sent_visible(self):
        return self.sent.is_visible()
