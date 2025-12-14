from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import re

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_text = page.locator('//h6[@data-testid="authentication-ui-course-title-text"]')
        self.email_input = page.locator('//div[@data-testid="login-form-email-input"]//input')
        self.password_input = page.locator('//div[@data-testid="login-form-password-input"]//input')
        self.login_button = page.locator('//button[@data-testid="login-page-login-button"]')
        self.registration_link = page.locator('//a[@data-testid="login-page-registration-link"]')

    def check_visible(self, email: str, password: str):
        expect(self.title_text).to_be_visible()
        expect(self.title_text).to_have_text('UI Course')

        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_have_value(password)

        expect(self.login_button).to_be_visible()

        expect(self.registration_link).to_be_visible()
        expect(self.registration_link).to_have_text('Registration')
    
    def fill_form(self, email, password):
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)

        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)
    
    def click_login_button(self):
        expect(self.login_button).to_be_enabled()
        self.login_button.click()
        self.check_current_url(re.compile('.*/#/dashboard'))
    
    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))