from playwright.sync_api import Page

class ResetPasswordPage:
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#reset-password-container')
        self.title = page.locator('#reset-password-title')
        self.message = page.locator('#reset-password-message')
        self.error = page.locator('#reset-password-error')
        self.form = page.locator('#reset-password-form')
        self.password = page.locator('#reset-password-password')
        self.confirm = page.locator('#reset-password-confirm')
        self.submit = page.locator('#reset-password-submit')

    def reset(self, pwd, confirm_pwd):
        self.password.fill(pwd)
        self.confirm.fill(confirm_pwd)
        self.submit.click()

    def is_error_visible(self):
        return self.error.is_visible()
