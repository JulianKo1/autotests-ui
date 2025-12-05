from playwright.sync_api import Playwright, Page
import pytest

@pytest.fixture
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//input')
    email_input.fill('user@gmail.com')

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//input')
    username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    password_input.fill('password')

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    context.storage_state(path='./browser-state.json')

@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='./browser-state.json')
    yield context.new_page()
    browser.close()

@pytest.fixture
def chromium_page_without_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    return page