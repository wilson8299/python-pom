import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    search_input = By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    search_button = By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def input_content(self, text):
        self.send_keys(self.search_input, text)

    def focus_searchbar(self):
        self.focus(self.search_input)

    def click_search_button(self):
        self.click(self.search_button)

    def page_screenshot(self):
        self.get_screenshot('search_page.png')