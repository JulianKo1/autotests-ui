import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.regression
def test_dashboard_displaying(dashboard_page: DashboardPage):
    dashboard_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    dashboard_page.navbar_component.check_visible('username')
    dashboard_page.check_visible_title()
    dashboard_page.check_visible_students_chart()
    dashboard_page.check_visible_activities_chart()
    dashboard_page.check_visible_courses_chart()
    dashboard_page.check_visible_scores_chart()