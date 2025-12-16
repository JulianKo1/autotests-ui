from unittest import TextTestResult
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.text import Text
from elements.image import Image

class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_card_title = Text(page, '//h6[@data-testid="course-widget-title-text"]', 'Title')
        self.course_card_image = Image(page, '//img[@data-testid="course-preview-image"]', 'Preview')
        self.course_card_min_score_text = Text(page, '//p[@data-testid="course-min-score-info-row-view-text"]', 'Min score')
        self.course_card_max_score_text = Text(page, '//p[@data-testid="course-max-score-info-row-view-text"]', 'Max score')
        self.course_card_estimated_time_text = Text(page, '//p[@data-testid="course-estimated-time-info-row-view-text"]', 'Estimated time')

        self.course_card_dropdown_menu_component = CourseViewMenuComponent(page)
    
    def check_visible(self, index, title: str, max_score, min_score, time_estim):
        self.course_card_title.check_visible(nth=index)
        self.course_card_title.check_have_text(text=title, nth=index)

        self.course_card_image.check_visible(nth=index)
        
        self.course_card_min_score_text.check_visible(nth=index)
        self.course_card_min_score_text.check_have_text(f'Min score: {min_score}', nth=index)

        self.course_card_max_score_text.check_visible(nth=index)
        self.course_card_max_score_text.check_have_text(f'Max score: {max_score}', nth=index)

        self.course_card_estimated_time_text.check_visible(nth=index)
        self.course_card_estimated_time_text.check_have_text(f'Estimated time: {time_estim}', nth=index)