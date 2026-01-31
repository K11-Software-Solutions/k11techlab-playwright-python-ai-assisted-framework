import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_parallel_pages():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page1 = await browser.new_page()
        page2 = await browser.new_page()
        await page1.goto('https://k11softwaresolutions.com')
        await page2.goto('https://playwright.dev')
        assert 'K11 Software Solutions' in await page1.title()
        assert 'Playwright' in await page2.title()
        await browser.close()
