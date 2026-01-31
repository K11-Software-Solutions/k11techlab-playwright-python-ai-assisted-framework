# Real Device Testing: iOS Safari (Cloud)

Playwright cannot directly automate Mobile Safari on real iOS devices locally. For real iOS Safari testing, use a device cloud provider such as BrowserStack.

## BrowserStack Playwright iOS Guide
- [BrowserStack Playwright on Real Devices](https://www.browserstack.com/docs/automate/playwright/ios)

## Example: browserstack.example.yml
```yaml
# Example BrowserStack config for Playwright
capabilities:
  browser: 'ios'
  device: 'iPhone 14'
  os_version: '16'
  real_mobile: true
  name: 'Playwright iOS Safari Test'
  build: 'playwright-ios-demo'
```

## How to Run
1. Sign up for a BrowserStack account and get your credentials.
2. Follow the [official guide](https://www.browserstack.com/docs/automate/playwright/ios) to set up your project.
3. Use the above config or capabilities in your Playwright test runner.

## Notes
- Cloud providers may require a different test runner or CLI for real device access.
- Video, logs, and screenshots are available in the BrowserStack dashboard.
- For Android cloud testing, see TestingBot, Sauce Labs, etc.

---

**CDP is Chromium-only. For real iOS Safari, use a device cloud.**
