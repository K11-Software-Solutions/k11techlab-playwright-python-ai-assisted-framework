from playwright.sync_api import Page

class ForgotPasswordPage:
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#forgot-password-container')
        self.form = page.locator('#forgot-password-form')
        self.email = page.locator('#forgot-password-email')
        self.submit = page.locator('#forgot-password-submit')
        self.message = page.locator('#forgot-password-message')
        self.error = page.locator('#forgot-password-error')

    def reset_password(self, email):
        self.email.fill(email)
        self.submit.click()

    def is_message_visible(self):
        return self.message.is_visible()
