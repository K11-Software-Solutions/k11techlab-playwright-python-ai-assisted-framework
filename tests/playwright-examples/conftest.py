import pytest

@pytest.fixture(scope="function", autouse=True)
def disable_playwright_tracing(context):
    pass
