import re
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.sausedemo.com/")
    page.locator("[data-test=\"username\"]").click()

    # ---------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)