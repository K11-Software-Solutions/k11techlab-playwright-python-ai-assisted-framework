import base64
from pathlib import Path

import pytest
import allure
from slugify import slugify

try:
    import pytest_html
except Exception:
    pytest_html = None


# Only register custom fixtures for k11-platform tests, not globally.
import sys
import os


def _mkdir_reports():
    for p in ("reports/screenshots", "reports/traces", "reports/videos"):
        Path(p).mkdir(parents=True, exist_ok=True)


def _getopt(config, name: str, default=None):
    """
    Robust option reader for k11 custom options only.
    """
    try:
        val = config.getoption(f"--k11{name}")
        return default if val is None else val
    except Exception:
        return default


def _store_screenshot_metadata(item, screenshot_path: str, test_name: str):
    with open(screenshot_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    item.screenshot_info = {"path": screenshot_path, "name": test_name, "base64": encoded}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture test result + attach screenshot image to pytest-html report (if installed).
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

    if report.when == "call" and pytest_html is not None:
        info = getattr(item, "screenshot_info", None)
        if info:
            extras = list(getattr(report, "extras", []))
            extras.append(
                pytest_html.extras.image(
                    info["base64"],
                    name=f"{info['name']}_screenshot",
                    mime_type="image/png",
                    extension="png",
                )
            )
            report.extras = extras


@pytest.fixture(autouse=True)
def k11_artifacts(request, page, context):
    """
    Autouse fixture for k11-platform tests only.
    """
    test_path = str(request.node.fspath)
    if "tests/k11-platform" not in test_path:
        # Do nothing for non-k11-platform tests
        yield
        return

    _mkdir_reports()

    screenshot_mode = _getopt(request.config, "screenshot", "off")  # off|on|only-on-failure
    tracing_mode = _getopt(request.config, "tracing", "off")        # off|on|retain-on-failure
    video_mode = _getopt(request.config, "video", "off")            # off|on|retain-on-failure

    # Start tracing (we manage tracing ourselves so we can attach to Allure reliably)
    tracing_started = False
    if tracing_mode in ("on", "retain-on-failure"):
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        tracing_started = True

    yield  # run the test

    # Determine failure
    failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    # ---------- TRACE ----------
    if tracing_started:
        from slugify import slugify
        trace_name = slugify(request.node.nodeid)[:150]
        trace_path = Path(f"reports/traces/{trace_name}.zip")
        if tracing_mode == "on" or (tracing_mode == "retain-on-failure" and failed):
            context.tracing.stop(path=str(trace_path))
            allure.attach.file(
                str(trace_path),
                name=f"{request.node.name}_trace",
                attachment_type=allure.attachment_type.ZIP,
            )
        else:
            # stop without saving
            context.tracing.stop()

    # ---------- SCREENSHOT ----------
    take_screenshot = (screenshot_mode == "on") or (
        screenshot_mode == "only-on-failure" and failed
    )
    if take_screenshot:
        from slugify import slugify
        shot_name = slugify(request.node.nodeid)[:150]
        shot_path = Path(f"reports/screenshots/{shot_name}.png")
        page.screenshot(path=str(shot_path), full_page=True)

        _store_screenshot_metadata(request.node, str(shot_path), request.node.name)

        allure.attach.file(
            str(shot_path),
            name=f"{request.node.name}_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    # ---------- VIDEO ----------
    # Video is finalized when the page is closed. Close it here so we can attach reliably.
    try:
        page.close()
    except Exception:
        pass

    if video_mode in ("on", "retain-on-failure"):
        try:
            if page.video:
                vpath = Path(page.video.path())
                if vpath.exists():
                    if video_mode == "on" or (video_mode == "retain-on-failure" and failed):
                        allure.attach.file(
                            str(vpath),
                            name=f"{request.node.name}_video",
                            attachment_type=allure.attachment_type.WEBM,
                        )
                    else:
                        # cleanup videos from passing tests (best effort)
                        try:
                            vpath.unlink()
                        except Exception:
                            pass
        except Exception:
            # If the underlying driver did not produce a video, ignore
            pass


# Register custom command-line options for Playwright sync fixtures

def pytest_addoption(parser):
    parser.addoption(
        "--k11browser",
        action="store",
        default="chromium",
        help="Browser to use for Playwright tests (chromium, firefox, webkit)"
    )
    parser.addoption(
        "--k11headed",
        action="store_true",
        default=False,
        help="Run browser in headed mode (default: headless)"
    )
    parser.addoption(
        "--k11video",
        action="store",
        default="off",
        help="Video recording: on, retain-on-failure, off"
    )
    parser.addoption(
        "--k11screenshot",
        action="store",
        default="off",
        help="Screenshot capture: on, only-on-failure, off"
    )
    parser.addoption(
        "--k11tracing",
        action="store",
        default="off",
        help="Tracing: on, retain-on-failure, off"
    )
