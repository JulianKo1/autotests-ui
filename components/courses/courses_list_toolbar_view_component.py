from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
from elements.button import Button
import re

class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_text = Text(page, '//h6[@data-testid="courses-list-toolbar-title-text"]', 'Toolbar title')
        self.add_course_button = Button(page, '//button[@data-testid="courses-list-toolbar-create-course-button"]', 'Create course button')
    
    def check_visible(self):
        self.title_text.check_visible()
        self.title_text.check_have_text(text='Courses')

        self.add_course_button.check_visible()

    def click_create_course_button(self):
        self.add_course_button.click()
        self.check_current_url(re.compile(".*/#/courses/create"))