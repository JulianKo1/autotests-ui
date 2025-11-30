from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://bpmsoft.ru')

    authorization_button = page.locator('//a[@href="//my.bpmsoft.ru/avtorizatsiya/"]')
    expect(authorization_button).not_to_be_visible()

    login_button = page.locator('//button[@data-action="log-in"]')
    login_button.click()

    expect(authorization_button).to_be_visible()
    authorization_button.click()

    email_input = page.locator('//input[@type="email" and @placeholder="Введите ваш корпоративный Email"]')
    email_input.fill('qwe')
    email_input.focus()
    page.keyboard.press('ControlOrMeta+A')
    page.keyboard.type("testkolabin@test.test")

    page.wait_for_timeout(3000)