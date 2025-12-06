from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class RegistrationPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')
    
    def check_visible_dashboard_page_title(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text('Dashboard')