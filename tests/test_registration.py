import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.registration
def test_registration_page(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form_component.check_visible(email='', username='', password='')
    registration_page.registration_form_component.click_login_link()
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form_component.fill_form(email='myuser@gmail.com', username='myusername', password='mypassword')
    registration_page.registration_form_component.check_visible(email='myuser@gmail.com', username='myusername', password='mypassword')
    registration_page.registration_form_component.click_registration_button()