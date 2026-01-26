'''
to execute the test - pytest
to run in headless mode - pytest --headless this is default mode
to run in headed mode - pytest --headed
to run in specific browser - pytest --browser=firefox
to run in specific browser with link - pytest --browser=firefox --base-url="https://www.saucedemo.com/"
to run with tracing - pytest --tracing on
to run with screenshots - pytest --screenshots on
to run with video - pytest --video on
to get report - pytest --html=report.html
we can provide the browser link during execution. use "/" in place of browser link in program.
to see the trace - playwright show-trace (copy the whole path along with the zip file name). this will open a gui to see the trace.
'''
import re  #import regular expressions
from playwright.sync_api import Page, expect
import pytest

# @pytest.mark.skip_browser("chromium")  #skip test in chrome browser

def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Swag Labs"))

def test_inventory_page(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    #expect the error message - use locator since the text is within an element
    expect(page.locator('h3')).to_contain_text(re.compile("Epic sadface: You can only access '/inventory.html' when you are logged in."))