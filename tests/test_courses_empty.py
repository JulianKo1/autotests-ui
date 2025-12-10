import pytest
from pages.courses_empty import CoursesEmptyPage

@pytest.mark.regression
def test_empty_course(courses_empty_page: CoursesEmptyPage):
    courses_empty_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_empty_page.navbar.check_visible('username')
    courses_empty_page.sidebar.check_visible()
    courses_empty_page.check_visible()