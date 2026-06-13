from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    #check the radio button
    radio_button = page.wait_for_selector('//input[@value="Male"]')
    radio_button.click()
    #page.wait_for_timeout(5000)
    #printing the testing status
    if radio_button.is_checked():
        print("Radio button is checked")
    else:
        print("Radio button is not checked")

    #check for checkbox
    checkbox = page.wait_for_selector('//input[@value="Movies"]')
    checkbox.check()
    if checkbox.is_checked():
        print("Checkbox is checked")
    else:
        print("Checkbox is not checked")
    page.wait_for_timeout(10000)