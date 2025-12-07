from math import exp
from playwright.sync_api import Page, expect
from requests import delete
from pages.base_page import BasePage

class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.courses_page_title = page.locator('//h6[@data-testid="courses-list-toolbar-title-text"]')
        self.create_course_button = page.locator('//button[@data-testid="courses-list-toolbar-create-course-button"]')

        # Блок при отсутствии курсов
        self.empty_folder_icon = page.locator('//*[@data-testid="courses-list-empty-view-icon"]')
        self.empty_page_title = page.locator('//h6[@data-testid="courses-list-empty-view-title-text"]')
        self.empty_page_description = page.locator('data-testid="courses-list-empty-view-description-text"')

        # Карточка курса
        self.course_title = page.locator('//h6[@data-testid="course-widget-title-text"]')
        self.course_image = page.locator('//img[@data-testid="course-preview-image"]')
        self.double_arrow_up_icon = page.locator('//*[@data-testid="KeyboardDoubleArrowUpIcon"]')
        self.max_score_text = page.locator('//p[@data-testid="course-max-score-info-row-view-text"]')
        self.double_arrow_down_icon = page.locator('//*[@data-testid="KeyboardDoubleArrowDownIcon"]')
        self.min_score_text = page.locator('//p[@data-testid="course-min-score-info-row-view-text"]')
        self.time_out_icon = page.locator('//*[@data-testid="AccessTimeOutlinedIcon"]')
        self.estimated_time_text = page.locator('//p[@data-testid="course-estimated-time-info-row-view-text"]')
        self.open_dropdown_button = page.locator('//button[@data-testid="course-view-menu-button"]')

        # Выпадающее меню курса
        self.edit_course_button = page.locator('//li[@data-testid="course-view-edit-menu-item"]')
        self.delete_course_button = page.locator('//li[@data-testid="course-view-delete-menu-item"]')

    def check_visible_courses_page_title(self):
        expect(self.courses_page_title).to_be_visible()
        expect(self.courses_page_title).to_have_text('Courses')
    
    def check_visible_courses_button(self):
        expect(self.create_course_button).to_be_visible()
    
    def click_create_course_button(self):
        self.create_course_button.click()
    
    def check_visible_empty_view(self):
        expect(self.empty_folder_icon).to_be_visible()

        expect(self.empty_page_title).to_be_visible()
        expect(self.empty_page_title).to_have_text('There is no results')

        expect(self.empty_page_description).to_be_visible()
        expect(self.empty_page_description).to_have_text('Results from the load test pipeline will be displayed here')
    
    def check_visible_course_card(self, index, title: str, max_score, min_score, estimated_time):
        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(title)

        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.double_arrow_up_icon.nth(index)).to_be_visible()
        expect(self.max_score_text.nth(index)).to_be_visible()
        expect(self.max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.double_arrow_down_icon.nth(index)).to_be_visible()
        expect(self.min_score_text.nth(index)).to_be_visible()
        expect(self.min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.time_out_icon.nth(index)).to_be_visible()
        expect(self.estimated_time_text.nth(index)).to_be_visible()
        expect(self.estimated_time_text.nth(index)).to_have_text(f'Estimated time: {estimated_time}')
    
    def click_edit_course_button(self, index: int):
        self.open_dropdown_button.nth(index).click()

        expect(self.edit_course_button(index)).to_be_visible()
        self.edit_course_button.nth(index).click()

    def click_delete_course_button(self, index):
        self.open_dropdown_button.nth(index).click()
        
        expect(self.delete_course_button.nth(index)).to_be_visible()
        self.delete_course_button.nth(index).click()        