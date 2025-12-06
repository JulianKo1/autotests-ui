from pages.registration_page import RegistrationPage

def test_registration_page_title(registration_page: RegistrationPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    registration_page.check_visible_dashboard_page_title()