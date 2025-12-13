from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import re

class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_text = page.locator('//h6[@data-testid="courses-list-toolbar-title-text"]')
        self.add_course_button = page.locator('//button[@data-testid="courses-list-toolbar-create-course-button"]')
    
    def check_visible(self):
        expect(self.title_text).to_be_visible()
        expect(self.title_text).to_have_text('Courses')

        expect(self.add_course_button).to_be_visible()

    def click_create_course_button(self):
        self.add_course_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))