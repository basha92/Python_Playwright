#this program is about using CSS selectors.
from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    page = browser.new_page()
    #--actions
    #--CSS Selectors are: ID - # operator, class - dot(.) operator, attribute - tagname[attribute="value"]
    #using ID operator
    #page.goto("https://demo.automationtesting.in/Index.html")
    #email_txt_box = page.wait_for_selector("#email")
    #email_txt_box.type('testmail@gamil.com')

    #login_button = page.wait_for_selector("#enterimg")
    #login_button.click()

    #page.wait_for_timeout(3000)
    #browser.close()

    #using attributes
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    password = page.wait_for_selector('input[type="password"]')
    password.type('admin123')
    submit = page.wait_for_selector('button[type="submit"]')
    submit.click()

    page.wait_for_timeout(3000)
    #browser.close()

