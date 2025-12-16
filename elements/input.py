from elements.base_element import BaseElement
from playwright.sync_api import Page, expect

class Input(BaseElement):
    def __init__(self, page: Page, locator: str, name: str):
        super().__init__(page, locator, name)
    
    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)
    
    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)