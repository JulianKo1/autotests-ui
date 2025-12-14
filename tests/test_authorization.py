import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password', [
    ('user.name@gmail.com', 'password'),
    ('  ', 'password'),
    ('user@gmail.com', '  ')
])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.fill_email_and_password_inputs(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

def test_successful_login(login_page: LoginPage, email='user@gmail.com', password='password'):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.sidebar.click_logout()
    login_page.login_form_component.fill_form(email, password)
    login_page.login_form_component.check_visible(email='user@gmail.com', password='password')
    login_page.login_form_component.click_login_button()
    