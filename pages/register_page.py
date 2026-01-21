from playwright.sync_api import Page

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator('#register-container')
        self.title = page.locator('#register-title')
        self.error = page.locator('#register-error')
        self.success = page.locator('#register-success')
        self.form = page.locator('#register-form')
        self.username = page.locator('#register-username')
        self.email = page.locator('#register-email')
        self.password = page.locator('#register-password')
        self.subscription = page.locator('#register-subscription')
        self.submit = page.locator('#register-submit')

    def register(self, user, email, pwd, subscription):
        # Wait for the registration form or username field to be visible
        try:
            self.username.wait_for(state="visible", timeout=10000)
        except Exception:
            try:
                self.form.wait_for(state="visible", timeout=10000)
            except Exception as e:
                # Debug: take screenshot and print current URL
                screenshot_path = "register_form_not_found.png"
                self.page.screenshot(path=screenshot_path, full_page=True)
                print(f"[DEBUG] Registration form not found. Screenshot saved to {screenshot_path}. Current URL: {self.page.url}")
                raise Exception(f"Registration form or username field not visible: {e}. Screenshot saved to {screenshot_path}. URL: {self.page.url}")
        self.username.fill(user)
        self.email.fill(email)
        self.password.fill(pwd)
        self.subscription.select_option(subscription)
        self.submit.click()

    def is_success_visible(self):
        return self.success.is_visible()
