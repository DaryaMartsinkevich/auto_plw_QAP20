import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_context(request):
    with sync_playwright() as p:
        browser_name = getattr(request, "param", "chromium")
        browser_type = getattr(p, browser_name, None)
        if browser_type is None:
            raise ValueError(f"Неверное имя браузера: {browser_name}")

        browser = browser_type.launch(headless=True)
        context = browser.new_context(record_video_dir="output/videos")

        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        try:
            yield context
        finally:
            context.tracing.stop(path=f"output/trace_{browser_name}.zip")
            browser.close()