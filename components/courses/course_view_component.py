from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.courses.course_view_menu_component import CourseViewMenuComponent

class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_card_title = page.locator('//h6[@data-testid="course-widget-title-text"]')
        self.course_card_image = page.locator('//img[@data-testid="course-preview-image"]')
        self.course_card_up_arrows_icon = page.locator('//*[@data-testid="KeyboardDoubleArrowUpIcon"]')
        self.course_card_down_arrows_icon = page.locator('//*[@data-testid="KeyboardDoubleArrowDownIcon"]')
        self.course_card_timeout_icon = page.locator('//*[@data-testid="AccessTimeOutlinedIcon"]')
        self.course_card_min_score_text = page.locator('//p[@data-testid="course-min-score-info-row-view-text"]')
        self.course_card_max_score_text = page.locator('//p[@data-testid="course-max-score-info-row-view-text"]')
        self.course_card_estimated_time_text = page.locator('//p[@data-testid="course-estimated-time-info-row-view-text"]')
        self.course_card_open_dropdown_button = page.locator('//button[@data-testid="course-view-menu-button"]')

        self.course_card_dropdown_menu_component = CourseViewMenuComponent(page)
    
    def check_visible(self, index, title: str, max_score, min_score, time_estim):
        expect(self.course_card_title.nth(index)).to_be_visible()
        expect(self.course_card_title.nth(index)).to_have_text(title)

        expect(self.course_card_open_dropdown_button.nth(index)).to_be_visible()
        
        expect(self.course_card_image.nth(index)).to_be_visible()

        expect(self.course_card_up_arrows_icon.nth(index)).to_be_visible()
        expect(self.course_card_down_arrows_icon.nth(index)).to_be_visible()
        expect(self.course_card_timeout_icon.nth(index)).to_be_visible()

        expect(self.course_card_max_score_text.nth(index)).to_be_visible()
        expect(self.course_card_max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.course_card_min_score_text.nth(index)).to_be_visible()
        expect(self.course_card_min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.course_card_estimated_time_text.nth(index)).to_be_visible()
        expect(self.course_card_estimated_time_text.nth(index)).to_have_text(f'Estimated time: {time_estim}')