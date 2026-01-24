# Playwright Device Demo Tests

This document describes the device emulation demo tests included in the framework, their purpose, and how to run them.

## Overview
The device demo tests showcase Playwright's ability to emulate real devices, including viewport, user agent, touch, orientation, geolocation, locale, timezone, dark mode, and network conditions. These tests are designed for demonstration and learning purposes.

## Test Scenarios
- **Device Matrix:** Runs the same test across multiple device profiles (e.g., iPhone, Pixel, iPad).
- **Orientation & Viewport:** Demonstrates portrait/landscape and viewport changes.
- **Touch Interactions:** Shows tap, drag-and-drop, and touch event handling.
- **Geolocation & Permissions:** Mocks geolocation and permission prompts.
- **Locale, Timezone, Dark Mode, Network:** Emulates locale, timezone, color scheme, and mocks API responses.
- **Visual Snapshot:** Captures screenshots for visual regression.

## How to Run
1. Ensure all dependencies are installed (`pip install -r requirements.txt`).
2. Run all device demo tests:
   ```sh
   python -m pytest tests/device_demo
   ```
3. To run a specific test:
   ```sh
   python -m pytest tests/device_demo/test_01_device_emulation_matrix.py
   ```

## Notes
- For full device emulation (especially touch), tests may require serving HTML via a local HTTP server, not file:// URLs.
- Artifacts (screenshots, videos) are saved in the `tests/device_demo/artifacts/` directory.
- All tests are marked with `@pytest.mark.device` and `@pytest.mark.demo` for easy filtering.

## Example Output
- Screenshots and videos for each device scenario
- Console output showing test results and assertions

---

For more details, see the test files in `tests/device_demo/`.
