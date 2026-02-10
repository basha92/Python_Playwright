import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(viewport={"width":1800,"height":1200})
    context = await browser.new_context()
    #setting the trace
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #opening new page
    page = await context.new_page()
    await page.goto("https://demoqa.com/select-menu")
    #--Action
    await page.get_by_text("Standard multi select").click()
    await page.select_option("select#cars", ["volvo", "Audi"])
    await page.screenshot(path="screenshots/multiselect.png", full_page=True)
    await context.tracing.stop(path="traces/multiselect_trace.zip")
    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())