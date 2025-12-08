from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.create_course_page_title = page.locator('//h6[@data-testid="create-course-toolbar-title-text"]')
        self.create_course_button = page.locator('//button[@data-testid="create-course-toolbar-create-course-button"]')

        # Блок с предпросмотром картинки
        self.empty_folder_icon = page.locator('//*[@data-testid="create-course-preview-empty-view-icon"]')
        self.empty_image_title = page.locator('//h6[@data-testid="create-course-preview-empty-view-title-text"]')
        self.empty_image_description = page.locator('//p[@data-testid="create-course-preview-empty-view-description-text"]')
        self.course_image = page.locator('//img[@data-testid="create-course-preview-image-upload-widget-preview-image"]')
        self.preview_image_upload_input = page.locator('//input[@data-testid="create-course-preview-image-upload-widget-input"]')
        
        # Блок с кнопкой загрузки и удаления изображения
        self.upload_image_icon = page.locator('//*[@data-testid="create-course-preview-image-upload-widget-info-icon"]')
        self.upload_image_title = page.locator('//p[@data-testid="create-course-preview-image-upload-widget-info-title-text"]')
        self.upload_image_description = page.locator('//span[@data-testid="create-course-preview-image-upload-widget-info-description-text"]')
        self.upload_image_button = page.locator('//label[@data-testid="create-course-preview-image-upload-widget-upload-button"]')
        self.remove_image_button = page.locator('//button[@data-testid="create-course-preview-image-upload-widget-remove-button"]')

        # Форма создания курса
        self.create_course_title_input = page.locator('//div[@data-testid="create-course-form-title-input"]//input')
        self.create_course_estimated_time_input = page.locator('//div[@data-testid="create-course-form-estimated-time-input"]//input')
        self.create_course_description_input = page.locator('//div[@data-testid="create-course-form-description-input"]//textarea[1]')
        self.create_course_max_score_title = page.locator('//div[@data-testid="create-course-form-max-score-input"]//label')
        self.create_course_max_score_input = page.locator('//div[@data-testid="create-course-form-max-score-input"]//input')
        self.create_course_min_score_title = page.locator('//div[@data-testid="create-course-form-min-score-input"]//label')
        self.create_course_min_score_input = page.locator('//div[@data-testid="create-course-form-min-score-input"]//input')

        # Заголовок и кнопка создания упражнения
        self.create_excercises_title = page.locator('//p[@data-testid="create-course-exercises-box-toolbar-title-text"]')
        self.create_excercises_button = page.locator('//button[@data-testid="create-course-exercises-box-toolbar-create-exercise-button"]')

        # Пустой блок для упражнений
        self.empty_excercises_icon = page.locator('//*[@data-testid="create-course-exercises-empty-view-icon"]')
        self.empty_excercises_title = page.locator('//h6[@data-testid="create-course-exercises-empty-view-title-text"]')
        self.empty_excercises_description = page.locator('//p[@data-testid="create-course-exercises-empty-view-description-text"]')

    def check_visible_create_course_title(self):
        expect(self.create_course_page_title).to_be_visible()
        expect(self.create_course_page_title).to_have_text('Create course')

    def click_create_course_button(self):
        expect(self.create_course_button).to_be_visible()
        expect(self.create_course_button).to_be_enabled()
        self.create_course_button.click()
    
    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_visible()
        expect(self.create_course_button).to_be_disabled()
    
    def upload_preview_image(self, file: str):
        self.preview_image_upload_input.set_input_files(file)

    def check_empty_view_preview_course_block(self):
        expect(self.empty_folder_icon).to_be_visible()

        expect(self.empty_image_title).to_be_visible()
        expect(self.empty_image_title).to_have_text('No image selected')
        
        expect(self.empty_image_description).to_be_visible()
        expect(self.empty_image_description).to_have_text('Preview of selected image will be displayed here')

    def check_preview_image(self):
        expect(self.course_image).to_be_visible()
    
    def check_visible_upload_image_block_before_uploading_image(self):
        expect(self.upload_image_icon).to_be_visible()
        
        expect(self.upload_image_title).to_be_visible()
        expect(self.upload_image_title).to_have_text('Tap on "Upload image" button to select file')
        
        expect(self.upload_image_description).to_be_visible()
        expect(self.upload_image_description).to_have_text('Recommended file size 540X300')

        expect(self.upload_image_button).to_be_visible()

        expect(self.remove_image_button).not_to_be_visible()
    
    def check_visible_upload_image_block_after_uploading_image(self):
        expect(self.upload_image_icon).to_be_visible()
        
        expect(self.upload_image_title).to_be_visible()
        expect(self.upload_image_title).to_have_text('Tap on "Upload image" button to select file')
        
        expect(self.upload_image_description).to_be_visible()
        expect(self.upload_image_description).to_have_text('Recommended file size 540X300')

        expect(self.upload_image_button).to_be_visible()

        expect(self.remove_image_button).to_be_visible()

    def check_visible_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value(title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)

        expect(self.create_course_description_input).to_be_visible()
        expect(self.create_course_description_input).to_have_value(description)

        expect(self.create_course_max_score_title).to_be_visible()
        expect(self.create_course_max_score_title).to_have_text('Max score')

        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_max_score_input).to_have_value(max_score)

        expect(self.create_course_min_score_title).to_be_visible()
        expect(self.create_course_min_score_title).to_have_text('Min score')

        expect(self.create_course_min_score_title).to_be_visible()
        expect(self.create_course_min_score_title).to_have_value(min_score)

    def fill_create_course_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_title_input.fill(title)
        self.create_course_estimated_time_input.fill(estimated_time)
        self.create_course_description_input.fill(description)
        self.create_course_max_score_input.fill(max_score)
        self.create_course_min_score_input.fill(min_score)

    def check_visible_create_excercise_title(self):
        expect(self.create_excercises_title).to_be_visible()
        expect(self.create_excercises_title).to_have_text('Exercises')

    def click_create_excercise_button(self):
        expect(self.create_excercises_button).to_be_visible()
        self.create_excercises_button.click()

    def check_visible_create_excercise_button(self):
        expect(self.create_excercises_button).to_be_visible()
    
    def check_visible_excercises_empty_view(self):
        expect(self.empty_folder_icon).to_be_visible()

        expect(self.empty_excercises_title).to_be_visible()
        expect(self.empty_excercises_title).to_have_text('There is no exercises')
        
        expect(self.empty_excercises_description).to_be_visible()
        expect(self.empty_excercises_description).to_have_text('Click on "Create exercise" button to create new exercise')
    
    def check_visible_create_excercise_form(self, index: int, title: str, description: str):
        excercise_subtitle = self.page.locator(f'//p[@data-testid="create-course-exercise-{index}-box-toolbar-subtitle-text"]')
        excercise_title_input = self.page.locator(f'//div[@data-testid="create-course-exercise-form-title-{index}-input"]//input')
        excercise_description_input = self.page.locator(f'data-testid="create-course-exercise-form-description-{index}-input"')

        expect(excercise_subtitle).to_be_visible()
        expect(excercise_subtitle).to_have_text(f'#{index} Exercise')

        expect(excercise_title_input).to_be_visible()
        expect(excercise_title_input).to_have_value(title)

        expect(excercise_description_input).to_be_visible()
        expect(excercise_description_input).to_have_value(description)
    
    def fill_create_excercise_form(self, index: int, title: str, description: str):
        excercise_title_input = self.page.locator(f'//div[@data-testid="create-course-exercise-form-title-{index}-input"]//input')
        excercise_description_input = self.page.locator(f'data-testid="create-course-exercise-form-description-{index}-input"')

        excercise_title_input.fill(title)
        expect(excercise_title_input).to_have_value(title)

        excercise_description_input.fill(description)
        expect(excercise_description_input).to_have_value(description)