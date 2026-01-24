import pytest

@pytest.mark.smoke
@pytest.mark.device
@pytest.mark.parametrize("device_name", ["iPhone 12", "Pixel 5"])
def test_device_emulation(browser, playwright, device_name):
    device = playwright.devices[device_name]
    context = browser.new_context(**device)
    page = context.new_page()

    page.goto("https://www.whatismybrowser.com/")
    ua = page.evaluate("navigator.userAgent")
    print(f"User agent for {device_name}: {ua}")

    expected = {"iPhone 12": "iphone", "Pixel 5": "android"}
    assert expected[device_name] in ua.lower()

    context.close()
