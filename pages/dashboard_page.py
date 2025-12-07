from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage (BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')

        self.students_title = page.locator('//h6[@data-testid="students-widget-title-text"]')
        self.students_chart = page.locator('//div[@data-testid="students-bar-chart"]')

        self.activities_title = page.locator('//h6[@data-testid="activities-widget-title-text"]')
        self.activities_chart = page.locator('//div[@data-testid="activities-line-chart"]')

        self.courses_title = page.locator('//h6[@data-testid="courses-widget-title-text"]')
        self.courses_chart = page.locator('//div[@data-testid="courses-pie-chart"]')

        self.scores_title = page.locator('//h6[@data-testid="scores-widget-title-text"]')
        self.scores_chart = page.locator('//div[@data-testid="scores-scatter-chart"]')
    
    def check_visible_title(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text('Dashboard')
    
    def check_visible_students_chart(self):
        expect(self.students_title).to_be_visible()
        expect(self.students_title).to_have_text('Students')
        expect(self.students_chart).to_be_visible()

    def check_visible_activities_chart(self):
        expect(self.activities_title).to_be_visible()
        expect(self.activities_title).to_have_text('Activities')
        expect(self.activities_chart).to_be_visible()

    def check_visible_courses_chart(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')
        expect(self.courses_chart).to_be_visible()

    def check_visible_scores_chart(self):
        expect(self.scores_title).to_be_visible()
        expect(self.scores_title).to_have_text('Scores')
        expect(self.scores_chart).to_be_visible()
    