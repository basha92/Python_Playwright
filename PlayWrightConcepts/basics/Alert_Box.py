from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    # selecting the locator for the alert box
    page.wait_for_selector('//a[@href="#OKTab"]').click()

    # wait for the dialog before clicking the button that triggers it
    dialog = page.wait_for_event("dialog")
    page.wait_for_selector('//button[@onclick="alertbox()"]').click()
    dialog.accept()

    page.wait_for_timeout(10000)