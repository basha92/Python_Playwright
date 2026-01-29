import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(viewport={"width":1800,"height":1200})
    #setting the trace
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = await context.new_page()
    await page.goto("https://demoqa.com/buttons")
    #-Actions
    #1. Click me button
    await page.get_by_role("heading", name="Buttons").click()
    await page.get_by_role("button", name="Click Me", exact=True).click()
    await page.get_by_text("You have done a dynamic click").click()
    await page.screenshot(path="screenshots/Click Me.png")
    #2. Double Click Me button
    await page.get_by_role("button", name="Double Click Me").dblclick()
    await page.get_by_text("You have done a dynamic click").click()
    await page.screenshot(path="screenshots/Double Click Me.png")
    #3. Right Click Me button
    await page.get_by_role("button", name="Right Click Me").click(button="right")
    await page.get_by_text("You have done a dynamic click").click()
    await page.screenshot(path="screenshots/Right Click Me.png")
     #stopping the trace
    await context.tracing.stop(path="traces/clickbutton_trace.zip")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
