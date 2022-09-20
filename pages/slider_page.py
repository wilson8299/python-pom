import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.slider = By.CSS_SELECTOR, '.sliderContainer > input'
        self.slider_value = By.CSS_SELECTOR, '.sliderContainer > span'

    def get_slider_value(self):
        return self.get_text(self.slider_value)

    def move_slider(self, *args):
        self.move_element_by_offset(self.slider, *args)
