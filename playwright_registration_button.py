from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_button_page = page.locator('//button[@data-testid="registration-page-registration-button"]')

    expect(registration_button_page).to_be_disabled()

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//input')
    email_input.fill('user@gmail.com')

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//input')
    username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    password_input.fill('password')

    expect(registration_button_page).to_be_enabled()