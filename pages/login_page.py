from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.courses.authentication.login_form_component import LoginFormComponent
from components.navigation.sidebar_component import SidebarComponent

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form_component = LoginFormComponent(page=page)   
        self.sidebar = SidebarComponent(page)