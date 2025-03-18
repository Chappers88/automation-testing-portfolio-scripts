# Scenario: Validation of data on a web page (Happy path, no screen shots)

from playwright.sync_api import sync_playwright, Page, expect

def test_validate_data():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        page.goto('https://playwright.dev/')
        header = page.get_by_text('Copyright © 2025 Microsoft')
        expect(header).to_be_visible()
        assert header.text_content() == 'Copyright © 2025 Microsoft'
        browser.close()

    