import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def user_data():
    return {"username": "test_user", "email": "test_user"}

def test_fixture(user_data):
    assert user_data["email"] == "test_user"

@pytest.fixture
def chromium():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()