# Real Android Device Testing with Playwright (CDP)

This folder contains a minimal demo for running Playwright tests on a real Android device using Chrome DevTools Protocol (CDP).

## Prerequisites
- Android device with Chrome installed
- USB debugging enabled
- ADB installed and device visible (`adb devices`)
- Chrome flag enabled: "Enable command line on non-rooted devices"

## Setup
1. Connect your Android device via USB and ensure it appears in `adb devices`.
2. On the device, open Chrome and enable the flag: `chrome://flags/#enable-command-line-on-non-rooted-devices`.
3. Forward the DevTools socket:
   ```sh
   adb forward tcp:9222 localabstract:chrome_devtools_remote
   ```
4. Run the test:
   ```sh
   python tests/device_demo/real_device/android_cdp/test_real_android_cdp.py
   ```

## Notes
- This works only for Chromium-based browsers (Chrome, Edge) on Android.
- Playwright's pytest plugin does not support CDP remote browsers directly; use standalone scripts.
