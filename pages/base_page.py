import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from utils.logger import Logger
from config.configuration import Global

class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.logger = Logger('base_page')
        self.chains = ActionChains(self.driver)
    
    def get_title(self):
        return self.driver.title

    def find_element(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element(loc[0], loc[1]))

    def find_elements(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_elements(loc[0], loc[1]))

    def send_keys(self, loc, keys):
        self.find_element(loc).send_keys(keys)
        self.logger.info(f'Input {keys} into {loc[1]}')

    def clear_content(self, loc):
        self.find_element(loc).clear()
        self.logger.info(f'Clear {loc[1]} content')

    def click(self, loc):
        self.find_element(loc).click()
        self.logger.info(f'Click {loc[1]} element')

    def get_screenshot(self, filename, loc = None):
        image_path = Global.IMAGE_DIR + filename
        if loc:
            self.find_element(loc).screenshot(image_path)
        else:
            self.driver.get_screenshot_as_file(image_path)
        self.logger.info(f'Save screenshot {image_path}')

    def focus(self, loc):
        element = self.find_element(loc)
        self.chains.move_to_element(element).perform()
        self.logger.info(f'Focus on {loc[1]} element')

    def left_click(self, loc):
        element = self.find_element(loc)
        self.chains.click(element).perform()
        self.logger.info(f'Left click {loc[1]} element')

    def right_click(self, loc):
        element = self.find_element(loc)
        self.chains.context_click(element).perform()
        self.logger.info(f'Right click {loc[1]} element')

    def double_click(self, loc):
        element = self.find_element(loc)
        self.chains.double_click(element).perform()
        self.logger.info(f'Double click {loc[1]} element')