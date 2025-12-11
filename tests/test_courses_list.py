from pages.courses_page import CoursesPage
import pytest

def test_courses_list(courses_page: CoursesPage):
    courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_page.course_card.check_visible(1, 'Тестовый курс', '52', '12', '2 недели')
    courses_page.course_card