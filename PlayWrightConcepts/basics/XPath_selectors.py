#using xpath selectors to login to orangehrm demo site
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #--actions
    #xpath selectors are: relative x path - //tagname[@attribute="value"]
    #username_element = page.wait_for_selector('//input[@name="username"]').type('Admin')
    #password_element = page.wait_for_selector('//input[@placeholder="Password"]').type('admin123')
    #login_button = page.wait_for_selector('//button[@type="submit"]').click()
    #page.wait_for_timeout(3000)
    
    #text selector - //tagname[text()="text value"]
    forgot_pwd = page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    page.wait_for_timeout(3000)

    #other selectors:
    #contains text - //tagname[contains(text(),"text value")]
    #contains attribute value - //tagname[contains(@attribute,"value")]

    #starts with text - //tagname[starts-with(text(),"text value")]
    #ends with text - //tagname[ends-with(text(),"text value")]
    #family selector - //tagname[@attribute="value"]//childtagname
    #following sibling - //tagname[@attribute="value"]/following-sibling::tagname
    #preceding sibling - //tagname[@attribute="value"]/preceding-sibling::tagname
    #ancestor selector - //tagname[@attribute="value"]/ancestor::tagname
    #descendant selector - //tagname[@attribute="value"]//descendant::tag