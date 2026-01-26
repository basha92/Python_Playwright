'''
Important notes:
1. Create a file that follows the test_ prefix convention, such as test_example.py, 
inside the current working directory or in a sub-directory with the code below. 
Make sure your test name also follows the test_ prefix convention.
2. Pytest - The pytest framework makes it easy to write small, readable tests, and can scale to 
support complex functional testing for applications and libraries.
3. To run the test, use the command: pytest <filename.py>
4. test runs in headless mode by default  means we can't see the browser UI when the test is running.
    To run the test in headed mode (with UI), we can set the headless parameter to False in the browser launch options.
5. to run in a browswer other than chromium, use the command: pytest <filename.py> --browser=firefox. chrome is default browser.

'''

import re  #import regular expressions
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/", headless=False)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/", headless=False)

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()









#first playwright script to open a browser and have a screenshot
#whenever we are writing a test in playwright need to import test and expect modules. 
# Test is used to define and run tests, while expect is used for assertions.
#sync mode - the execution takes place line by line. It will block other lines of code until the curent line is executed. 
# Useful for simple scripts and debugging.

#Async mode - the execution does not block other lines of code. It allows multiple operations to run concurrently.
# Useful for complex scenarios and performance optimization.

#sync mode
'''from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://demoqa.com/")
    page.screenshot(path="demo.png")
    browser.close()'''

#async mode
'''import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://demoqa.com/")
        await page.screenshot(path="demo.png")
        await browser.close()

asyncio.run(main())'''


