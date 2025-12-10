from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from typing import Pattern

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.item_icon = page.locator(f'//div[@data-testid="{identifier}-drawer-list-item-icon"]')
        self.item_title = page.locator(f'//div[@data-testid="{identifier}-drawer-list-item-title-text"]//span')
        self.item_button = page.locator(f'//div[@data-testid="{identifier}-drawer-list-item-button"]')

    def check_item_visible(self, title: str):
        expect(self.item_icon).to_be_visible()
        
        expect(self.item_title).to_be_visible()
        expect(self.item_title).to_have_text(title)

        expect(self.item_button).to_be_visible()
    
    def navigate(self, expected_url: Pattern[Page]):
        self.item_button.click()
        expect(self.page).to_have_url(expected_url)