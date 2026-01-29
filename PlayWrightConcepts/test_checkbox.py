import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    #launchint the browser and setting the view
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(viewport={"width":1800,"height":1200})
    #setting the trace
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #opening new page
    page = await context.new_page()
    await page.goto("https://demoqa.com/checkbox")
    #-actions
    await page.get_by_role("button", name="Toggle").click()
    await page.get_by_role("listitem").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    await page.get_by_role("listitem").filter(has_text=re.compile(r"^Documents$")).get_by_label("Toggle").click()
    await page.get_by_role("listitem").filter(has_text=re.compile(r"^Downloads$")).get_by_label("Toggle").click()
    #taking screenshot
    await page.screenshot(path="screenshots/emptycheckbox.png")
    await page.locator("label").filter(has_text="Home").get_by_role("img").first.click()
    await page.screenshot(path="screenshots/selectedcheckbox.png")
    #-Assertions
    await page.get_by_text("Home", exact=True).click()
    await page.get_by_text("Home", exact=True).click()
    #stopping the trace
    await context.tracing.stop(path="traces/checkbox_trace.zip")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
