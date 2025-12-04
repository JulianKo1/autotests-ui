from playwright.sync_api import Page
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_registration(chromium_page_with_state: Page):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//input')
    email_input.fill('user@gmail.com')

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//input')
    username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    password_input.fill('password')

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    page = chromium_page_with_state

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
