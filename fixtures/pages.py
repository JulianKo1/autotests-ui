import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_page import CoursesPage
from pages.create_course_page import CreateCoursePage
from pages.courses_empty import CoursesEmptyPage

@pytest.fixture
def login_page(chromium_page_without_state: Page) -> LoginPage:
    return LoginPage(page=chromium_page_without_state)

@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page_with_state: Page) -> RegistrationPage:
    return DashboardPage(page=chromium_page_with_state)

@pytest.fixture
def courses_page(chromium_page_with_state: Page) -> CoursesPage:
    return CoursesPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(chromium_page_with_state)

@pytest.fixture
def courses_empty_page(chromium_page_with_state: Page) -> CoursesEmptyPage:
    return CoursesEmptyPage(chromium_page_with_state)