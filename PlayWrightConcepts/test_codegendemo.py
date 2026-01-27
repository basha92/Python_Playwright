'''
to generate the code, use playwright codegen https://www.saucedemo.com/ --target pytest or you can change the target language in the codegen window
to emulate the code in a device, use playwright codegen --device="iPhone 11 Pro" https://www.saucedemo.com/ --target pytest
to run only particular test using the pytest ini, use python -m pytest -k test_codegendemo.py (name of the file) in the terminal
to have the screen size and color, use playwright codegen --viewport-size="800,600"  --color-scheme=dark https://www.saucedemo.com/
'''



import pytest
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    #going to the page
    page.goto("https://www.saucedemo.com/")
    #filling user name: standard_user
    page.locator("[data-test=\"username\"]").fill("standard_user")
    #filling password: secret_sauce
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    #clicking on login button
    page.locator("[data-test=\"login-button\"]").click()
