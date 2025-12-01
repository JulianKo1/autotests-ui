from math import exp
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
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
    
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='./browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    page_title = page.locator('//h6[@data-testid="courses-list-toolbar-title-text"]')

    expect(page_title).to_be_visible()
    expect(page_title).to_have_text(expected='Courses')

    no_results_title = page.locator('//h6[@data-testid="courses-list-empty-view-title-text"]')
    expect(no_results_title).to_be_visible()
    expect(no_results_title).to_have_text(expected='There is no results')

    empty_folder_svg = page.locator("//*[local-name()='svg' and @data-testid='courses-list-empty-view-icon']")
    expect(empty_folder_svg).to_be_visible()

    no_results_description = page.locator('//p[@data-testid="courses-list-empty-view-description-text"]')
    expect(no_results_description).to_be_visible()
    expect(no_results_description).to_have_text('Results from the load test pipeline will be displayed here')