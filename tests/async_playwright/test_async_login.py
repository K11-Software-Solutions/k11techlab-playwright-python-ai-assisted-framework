
import re
import pytest
from playwright.async_api import async_playwright, expect

class AsyncLoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('#login-username')
        self.password = page.locator('#login-password')
        self.submit = page.locator('#login-submit')
        self.error = page.locator('#login-error')

    async def login(self, username, password):
        await self.username.fill(username)
        await self.password.fill(password)
        await self.submit.click()

    async def get_login_error(self):
        return self.error

@pytest.mark.asyncio
async def test_valid_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://k11softwaresolutions.com/login')
        login = AsyncLoginPage(page)
        await login.login('testuser', 'testpass')
        # Wait for dashboard URL and then check for dashboard welcome text
        await expect(page).to_have_url(re.compile(r"/dashboard"), timeout=10000)
        await expect(page.locator("text=Manage your account and view updates")).to_be_visible(timeout=10000)
        await browser.close()
