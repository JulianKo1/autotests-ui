from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.button import Button

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page): 
        super().__init__(page)
        
        self.dropdown_edit_button = Button(page, '//li[@data-testid="course-view-edit-menu-item"]', 'Edit')
        self.dropdown_delete_button = Button(page, '//li[@data-testid="course-view-delete-menu-item"]', 'Delete')
        self.dropdown_open_menu_button = Button(page, '//button[@data-testid="course-view-menu-button"]', 'Menu')

    def click_edit_button(self, index: int):
        self.dropdown_open_menu_button.click(nth=index)

        self.dropdown_edit_button.check_visible(nth=index)
        self.dropdown_edit_button.click(nth=index)

    def click_delete_button(self, index: int):
        self.dropdown_open_menu_button.click(nth=index)
        
        self.dropdown_delete_button.check_visible(nth=index)
        self.dropdown_delete_button.click(nth=index)
