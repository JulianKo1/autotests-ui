from elements.base_element import BaseElement
from playwright.sync_api import Page, expect

class Button(BaseElement):
    def __init__(self, page: Page, locator: str, name: str):
        super.__init__(page, locator, name)
    
    def check_disabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()
    
    def check_enabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()