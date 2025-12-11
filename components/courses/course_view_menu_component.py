from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page): 
        super().__init__(page)

        self.dropdown_edit_button = page.locator('//li[@data-testid="course-view-edit-menu-item"]')
        self.dropdown_delete_button = page.locator('//li[@data-testid="course-view-delete-menu-item"]')
        self.dropdown_open_menu_button = page.locator('//button[@data-testid="course-view-menu-button"]')

    def click_edit_button(self, index):
        self.dropdown_open_menu_button.nth(index).click()

        expect(self.dropdown_edit_button.nth(index)).to_be_visible()
        self.dropdown_edit_button.nth(index).click()

    def click_delete_button(self, index):
        self.dropdown_open_menu_button.nth(index).click()
        
        expect(self.dropdown_delete_button.nth(index)).to_be_visible()
        self.dropdown_delete_button.nth(index).click()
