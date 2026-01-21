from playwright.sync_api import Page

class LoginPage:
    """Page Object Model class for the Login Page, using element IDs from the prompt."""
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#login-container')
        self.title = page.locator('#login-title')
        self.error = page.locator('#login-error')
        self.form = page.locator('#login-form')
        self.username = page.locator('#login-username')
        self.password = page.locator('#login-password')
        self.forgot_password_link = page.locator('#login-forgot-password-link')
        self.forgot_link = page.locator('#login-forgot-link')
        self.submit = page.locator('#login-submit')
        self.register_link = page.locator('#login-register-link')
        self.register_here = page.locator('#login-register-here')

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        # Press Enter in the password field to submit the form
        self.password.press("Enter")

    def is_error_visible(self):
        return self.error.is_visible()

    def click_forgot_password(self):
        self.forgot_link.click()

    def click_register_here(self):
        self.register_here.click()

    def set_email(self, email):
        self.username.fill(email)

    def set_password(self, password):
        self.password.fill(password)

    def get_login_error(self):
        """
        Return the error message locator if login fails.
        Example use:
            error_text = login_page.get_login_error().inner_text()
        """
        return self.error

    def click_login(self):
        """Click the login/submit button on the login form."""
        self.submit.click()
