from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
import re

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page=page, identifier='logout')
        self.dashboard_list_item = SidebarListItemComponent(page=page, identifier='dashboard')
        self.courses_list_item = SidebarListItemComponent(page=page, identifier='courses')
    
    def check_visible(self):
        self.logout_list_item.check_item_visible(title='Logout')
        self.dashboard_list_item.check_item_visible(title='Dashboard')
        self.courses_list_item.check_item_visible(title='Courses')
    
    def click_logout(self):
        self.logout_list_item.navigate(re.compile('.*/#/auth/login'))

    def click_courses(self):
        self.courses_list_item.navigate(re.compile('.*/#/courses'))
    
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile('.*/#/dashboard'))