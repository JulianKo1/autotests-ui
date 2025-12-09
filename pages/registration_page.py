from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator('//h6[@data-testid="authentication-ui-course-title-text"]')
        self.email_input = page.locator('//div[@data-testid="registration-form-email-input"]//input')
        self.username_input = page.locator('//div[@data-testid="registration-form-username-input"]//input')
        self.password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
        self.registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
        self.login_link = page.locator('//a[@data-testid="registration-page-login-link"]')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        expect(self.registration_button).to_be_visible()
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def click_login_link(self):
        expect(self.login_link).to_be_visible()
        self.login_link.click()
        
