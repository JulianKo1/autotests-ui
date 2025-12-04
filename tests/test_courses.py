from playwright.sync_api import Page, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):        
    page = chromium_page_with_state

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    page_title = page.locator('//h6[@data-testid="courses-list-toolbar-title-text"]')

    expect(page_title).to_be_visible()
    expect(page_title).to_have_text(expected='Courses')

    no_results_title = page.locator('//h6[@data-testid="courses-list-empty-view-title-text"]')
    expect(no_results_title).to_be_visible()
    expect(no_results_title).to_have_text(expected='There is no results')

    empty_folder_svg = page.locator("//*[local-name()='svg' and @data-testid='courses-list-empty-view-icon']")
    expect(empty_folder_svg).to_be_visible()

    no_results_description = page.locator('//p[@data-testid="courses-list-empty-view-description-text"]')
    expect(no_results_description).to_be_visible()
    expect(no_results_description).to_have_text('Results from the load test pipeline will be displayed here')