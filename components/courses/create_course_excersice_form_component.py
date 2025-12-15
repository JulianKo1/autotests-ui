from components.base_component import BaseComponent, expect
from elements.button import Button
from elements.text import Text
from elements.input import Input
from playwright.sync_api import Page

class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_excercise_button = Button(page=page, locator='create-course-exercise-{index}-box-toolbar-delete-exercise-button', name='Delete excercise')
        self.subtitle_text = Text(page=page, locator='create-course-exercise-{index}-box-toolbar-subtitle-text', name='Excercise subtitle')
        self.title_input = Input(page=page, locator='create-course-exercise-form-title-{index}-input', name='Title')
        self.description_input = Input(page=page, locator='create-course-exercise-form-description-{index}-input', name='Description')

    def click_delete_button(self, index: int):
        self.delete_excercise_button.click(index=index)

    def check_visible(self, index: int, title: str, description: str):
        self.subtitle_text.check_visible(index=index)
        self.subtitle_text.check_have_text(index=index)

        self.title_input.check_visible(index=index)
        self.title_input.check_have_value(value=title, index=index)

        self.description_input.check_visible(index=index)
        self.description_input.check_have_value(value=description, index=index)

    def fill(self, index: int, title: str, description: str):
        self.title_input.fill(value=title, index=index)
        self.title_input.check_have_value(value=title, index=index)

        self.description_input.fill(value=description, index=index)
        self.description_input.check_have_value(value=description, index=index)
