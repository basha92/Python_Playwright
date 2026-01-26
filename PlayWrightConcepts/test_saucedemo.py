
import re  #import regular expressions
from playwright.sync_api import Page, expect
import pytest

def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Swag Labs"))

def test_inventory_page(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    #expect the error message
    expect(page.locator('h3')).to_contain_text(re.compile("Epic sadface: You can only access '/inventory.html' when you are logged in."))