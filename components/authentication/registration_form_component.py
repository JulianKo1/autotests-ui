from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import re

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_text = page.locator('//h6[@data-testid="authentication-ui-course-title-text"]')
        self.email_input = page.locator('//div[@data-testid="registration-form-email-input"]//input')
        self.username_input = page.locator('//div[@data-testid="registration-form-username-input"]//input')
        self.password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
        self.registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
        self.login_link = page.locator('//a[@data-testid="registration-page-login-link"]')
    
    def check_visible(self, email: str, username: str, password: str):
        expect(self.title_text).to_be_visible()
        expect(self.title_text).to_have_text('UI Course')

        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.username_input).to_be_visible()
        expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)

        expect(self.registration_button).to_be_visible()

        expect(self.login_link).to_be_visible()
        expect(self.login_link).to_have_text('Login')
    
    def fill_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)
    
    def click_registration_button(self):
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()
        self.check_current_url(re.compile(".*/#/dashboard"))
    
    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))