#this is about launching the chromium browser and navigating to a website
#since it is basics, used all as pyython scripts. For tests, we need to use the pytest framework.
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #launching the browser
    page = browser.new_page() #telling that we need a new page
    page.goto("https://demoqa.com/") #telling which page to be opened
    print("chromium browser launched and the page is opened")
    print(page.title()) #printing the page title
    page.wait_for_timeout(3000) #waiting fo the the things to happen
    browser.close() #closing the browser