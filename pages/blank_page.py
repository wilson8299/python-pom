import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BlankPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.link = By.CSS_SELECTOR, '#content > div > a'
        self.header = By.CSS_SELECTOR, 'body > div > h3'

    def click_link(self):
        self.click(self.link)

    def get_new_page_header(self):
        self.switch_window(1)
        return self.get_text(self.header)