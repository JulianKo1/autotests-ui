import playwright
from playwright.sync_api import Page
import pytest
from pages.create_course_page import CreateCoursePage
from pages.courses_page import CoursesPage

@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_page: CoursesPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.empty_view.check_visible(title='No image selected', description='Preview of selected image will be displayed here')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_empty_view_preview_course_block()
    create_course_page.check_visible_upload_image_block_before_uploading_image()
    create_course_page.check_visible_create_course_form(title='', description='', estimated_time='', max_score="0", min_score="0")
    create_course_page.check_visible_create_excercise_title()
    create_course_page.check_visible_create_excercise_button()
    create_course_page.check_visible_excercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/test.png')
    create_course_page.check_visible_upload_image_block_after_uploading_image()
    create_course_page.check_preview_image()
    create_course_page.fill_create_course_form(title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10')
    create_course_page.click_create_course_button()
    # courses_page.check_visible_courses_page_title()
    # courses_page.check_visible_courses_button()
    courses_page.course_card.check_visible(index=0, title='Playwright', max_score='100', min_score='10', time_estim='2 weeks')
    courses_page.toolbar.check_visible()
    courses_page.toolbar.click_create_course_button()