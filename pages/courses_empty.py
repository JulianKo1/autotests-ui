from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent

class CoursesEmptyPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page=page)
        self.sidebar = SidebarComponent(page=page)

        self.courses_empty_folder_image = page.locator('//*[@data-testid="courses-list-empty-view-icon"]')
        self.courses_empty_title = page.locator('//h6[@data-testid="courses-list-empty-view-title-text"]')
        self.courses_empty_description = page.locator('//p[@data-testid="courses-list-empty-view-description-text"]')
    
    def check_visible(self):
        expect(self.courses_empty_folder_image).to_be_visible()

        expect(self.courses_empty_title).to_be_visible()
        expect(self.courses_empty_title).to_have_text('There is no results')

        expect(self.courses_empty_description).to_be_visible()
        expect(self.courses_empty_description).to_have_text('Results from the load test pipeline will be displayed here')