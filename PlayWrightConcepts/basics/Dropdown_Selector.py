#contains selectors for drop down list
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    #--actions
    #1. finding the dropdown
    #select_dropdown = page.locator('//select[contains(@id,"Skills")]')
    #select_dropdown.click()
    #2. selecting skills from drop down list using contains selector
    #select_dropdown.select_option(label="AutoCAD")
    
    #the above way is ususlly used in selenium. 
    # In playwright we can directly select the option without clicking the dropdown list. 
    # Below is the way to do it in playwright. select drop down and option in one line.
    page.select_option('//select[contains(@id,"Skills")]', label="AutoCAD")


    page.wait_for_timeout(3000)
    browser.close()

