# Scenario: Validation of landing on a home page (Happy path, no screen shots)

from playwright.sync_api import sync_playwright

def test_check_homepage():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        page.goto('https://playwright.dev/')
        browser.close()
