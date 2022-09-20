import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.alert_button = By.CSS_SELECTOR, '#content > div > ul > li:nth-child(1) > button'
        self.confirm_button = By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > button'
        self.prompt_button = By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > button'
        self.result = By.ID, 'result'

    def get_result_content(self):
        return self.get_text(self.result)

    def click_alert_button(self):
        self.click(self.alert_button)

    def click_confirm_button(self):
        self.click(self.confirm_button)

    def click_prompt_button(self):
        self.click(self.prompt_button)

    def switch_to_alert(self):
        return self.switch_alert

    def accept_alert(self):
        self.alert_process('accept')

    def dismiss_alert(self):
        self.alert_process('dismiss')

    def type_alert_message(self, message):
        self.alert_process('message', message)