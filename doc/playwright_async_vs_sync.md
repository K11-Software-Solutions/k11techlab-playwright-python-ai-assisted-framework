
# Async vs Sync Playwright in Python: When to Use Each

## Overview
Playwright for Python offers both synchronous and asynchronous APIs. Choosing between them depends on your project needs, test complexity, and integration requirements. This article explains the differences, use cases, and best practices for each approach in test automation.

---

## Synchronous Playwright

### What is it?
- Uses blocking calls (no `async`/`await` required)
- Simple, linear code flow
- Ideal for most standard test cases

### When to Use Sync API
- **Simple test scripts**: Most UI automation, smoke, and regression tests
- **Quick prototyping**: Fast to write and debug
- **Integration with sync frameworks**: Works out-of-the-box with pytest, unittest, etc.
- **No need for parallel browser/page actions**

### Example
```python
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com')
        page.fill('#username', 'user')
        page.fill('#password', 'pass')
        page.click('button[type=submit]')
        assert page.url == 'https://example.com/dashboard'
        browser.close()
```

---

## Asynchronous Playwright

### What is it?
- Uses `async`/`await` syntax
- Non-blocking, can run multiple tasks concurrently
- Requires an async test runner (e.g., pytest-asyncio)

### When to Use Async API
- **Complex workflows**: Multiple browsers/pages, parallel actions
- **Performance**: Speed up tests by running tasks concurrently
- **Integration with async systems**: If your app/test utilities use async (e.g., async DB, APIs)
- **Advanced scenarios**: Real-time event handling, websockets, etc.

### Example
```python
import pytest
import asyncio
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_login_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')
        await page.fill('#username', 'user')
        await page.fill('#password', 'pass')
        await page.click('button[type=submit]')
        assert page.url == 'https://example.com/dashboard'
        await browser.close()
```

---

## How to Choose
- **Default to sync** for most test automation unless you need async features.
- **Use async** if:
    - You need to run multiple browser/page actions in parallel
    - Your framework or utilities are async
    - You want maximum performance for large-scale, concurrent tests
- **Mixing sync and async is not recommended**. Pick one style per test/module.

---

## Best Practices
- Use sync for simplicity and compatibility
- Use async for advanced, concurrent, or performance-critical scenarios
- Always await async Playwright calls
- Use pytest-asyncio for async tests with pytest
- Keep your Page Object Model (POM) consistent: sync or async methods only

---

## Summary Table
| Use Case                        | Recommended API |
|----------------------------------|-----------------|
| Simple UI tests                  | Sync            |
| Data-driven, smoke, regression   | Sync            |
| Parallel browser/page actions    | Async           |
| Real-time/event-driven scenarios | Async           |
| Integration with async systems   | Async           |
| Quick prototyping                | Sync            |

---

---

## Parallel Test Execution: Sync vs Async

### Sync Playwright (pytest-xdist)
- You can run multiple test functions or files in parallel using pytest-xdist (e.g., pytest -n 4).
- Each test runs in a separate process, but browser/page actions inside a single test are sequential.
- Use sync mode for parallelizing test suites, not for parallel actions within a single test.

### Async Playwright
- True parallel browser/page actions within a single test are only possible with async Playwright.
- Use async/await to run multiple pages, browsers, or tasks concurrently in one test function.
- Ideal for scenarios needing simultaneous actions, real-time events, or performance testing.

### Summary
- **Sync + pytest-xdist:** Parallel test files/functions, sequential actions inside each test.
- **Async:** Parallel actions inside a single test, plus you can still use pytest-xdist for suite-level parallelism.

---

## References
- [Playwright Python Docs](https://playwright.dev/python/docs/intro)
- [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)
- [Async Programming in Python](https://docs.python.org/3/library/asyncio.html)

---

*Choose the API that best fits your test needs. Both sync and async Playwright are fully supported in modern Python automation frameworks.*
