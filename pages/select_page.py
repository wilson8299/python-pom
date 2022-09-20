import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SelectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.select = By.ID, 'dropdown'

    def get_select_text(self):
        return self.get_selected_option(self.select).text

    def set_select_by_index(self, index):
        select = self.get_select_element(self.select)
        select.select_by_index(index)

    def set_select_by_value(self, value):
        select = self.get_select_element(self.select)
        select.select_by_value(value)

    def set_select_by_visible_text(self, text):
        select = self.get_select_element(self.select)
        select.select_by_visible_text(text)

    def t(self):
        self.find_elements((By.ID, 'aaa'))