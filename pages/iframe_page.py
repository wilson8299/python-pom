import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class IframePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = By.CSS_SELECTOR, '#content > div > h3'
        self.iframe_content = By.CSS_SELECTOR, '#tinymce > p'

    def switch_to_iframe(self):
        self.switch_frame(0)

    def switch_to_default_content(self):
        self.switch_frame()

    def get_header_content(self):
        return self.get_text(self.header)

    def get_iframe_content(self):
        return self.get_text(self.iframe_content)