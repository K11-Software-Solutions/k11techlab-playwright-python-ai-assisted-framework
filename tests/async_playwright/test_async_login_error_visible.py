import pytest
from playwright.async_api import async_playwright

class AsyncLoginPage:
    """Async Page Object Model for Login Page."""
    def __init__(self, page):
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

    async def login(self, username, password):
        await self.username.fill(username)
        await self.password.fill(password)
        await self.password.press("Enter")

    async def is_error_visible(self):
        return await self.error.is_visible()

    async def get_login_error_text(self):
        return await self.error.inner_text()

@pytest.mark.asyncio
async def test_login_error_visible():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://k11softwaresolutions.com/login')
        login = AsyncLoginPage(page)
        await login.login('invaliduser', 'invalidpass')
        assert await login.is_error_visible()
        error_text = await login.get_login_error_text()
        print(f"Login error: {error_text}")
        await browser.close()
