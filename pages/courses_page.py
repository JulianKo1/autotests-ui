from math import exp
from playwright.sync_api import Page, expect
from requests import delete
from pages.base_page import BasePage
from components.courses.course_view_component import CourseViewComponent

class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_card = CourseViewComponent(page)