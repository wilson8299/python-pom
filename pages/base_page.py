import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from utils.logger import Logger
from config.configuration import Global
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.logger = Logger('Page')
        self.ac = ActionChains(self.driver)
    
    def get_title(self):
        return self.driver.title

    def find_element(self, loc):
        try:
            element = WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element(loc[0], loc[1]));
        except Exception as e:
            self.logger.error(f'Error when find element {loc}')
            self.logger.exception(e)
        else:
            return element

    def find_elements(self, loc):
        try:
            element = WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_elements(loc[0], loc[1]))
        except Exception as e:
            self.logger.error(f'Error when find elements {loc}')
            self.logger.exception(e)
        else:
            return element

    def switch_window(self, index):
        try:
            self.driver.switch_to.window(self.driver.window_handles[index])
        except Exception as e:
            self.logger.error('Error when switching browser window')
            self.logger.exception(e)

    def switch_frame(self, index=None, id_name=None, loc=None):
        try:
            self.driver.switch_to.default_content()
            if id_name is not None:
                self.driver.switch_to.frame(id_name)
            elif index is not None:
                self.driver.switch_to.frame(index)
            elif loc is not None:
                iframe = self.find_element(loc)
                self.driver.switch_to.frame(iframe)
        except Exception as e:
            self.logger.error('Error when switching frame')
            self.logger.exception(e)

    def switch_alert(self):
        try:
            alert = self.driver.switch_to.alert
        except Exception as e:
            self.logger.error(f'Error when switching alert pop')
            self.logger.exception(e)
        else:
            return alert

    def alert_process(self, process, message=None):
        try:
            alert = self.switch_alert()
            if(process == 'accept'):
                alert.accept()
            elif(process == 'dismiss'):
                alert.dismiss()
            elif(process == 'message'):
                alert.send_keys(message)
        except Exception as e:
            self.logger.error(f'Error when process alert')
            self.logger.exception(e)   

    def send_keys(self, loc, *keys):
        try:
            self.find_element(loc).send_keys(keys)
        except Exception as e:
            self.logger.error('Error when send keys')
            self.logger.exception(e)

    def get_text(self, loc):
        try:
            text = self.find_element(loc).text
        except Exception as e:
            self.logger.error('Error when get text')
            self.logger.exception(e)
        else:
            return text

    def get_property(self, loc, property_name):
        try:
            property = self.find_element(loc).get_property(property_name)
        except Exception as e:
            self.logger.error('Error when get property')
            self.logger.exception(e)
        else:
            return property

    def get_attribute(self, loc, attribute_name):
        try:
            attribute = self.find_element(loc).get_attribute(attribute_name)
        except Exception as e:
            self.logger.error('Error when get attribute')
            self.logger.exception(e)
        else:
            return attribute

    def clear_content(self, loc):
        try:
            self.find_element(loc).clear()
        except Exception as e:
            self.logger.error(f'Error when clear locator {loc}')
            self.logger.exception(e)

    def get_select_element(self, loc):
        return Select(self.find_element(loc))

    def get_selected_option(self, loc):
        return self.get_select_element(loc).first_selected_option

    def get_screenshot(self, filename, loc = None):
        image_path = Global.IMAGE_DIR + filename
        if loc:
            self.find_element(loc).screenshot(image_path)
        else:
            self.driver.get_screenshot_as_file(image_path)

    def click(self, loc):
        try:
            self.find_element(loc).click()
        except Exception as e:
            self.logger.error(f'Error when click locator {loc}')
            self.logger.exception(e)

    def left_click(self, loc):
        try:
            element = self.find_element(loc)
            self.ac.click(element).perform()
        except Exception as e:
            self.logger.error(f'Error when click {loc} with the left button')
            self.logger.exception(e)

    def right_click(self, loc):
        try:
            element = self.find_element(loc)
            self.ac.context_click(element).perform()
        except Exception as e:
            self.logger.error(f'Error when click {loc} with the right button')
            self.logger.exception(e)

    def double_click(self, loc):
        try:
            element = self.find_element(loc)
            self.ac.double_click(element).perform()
        except Exception as e:
            self.logger.error(f'Error when double click {loc}')
            self.logger.exception(e)

    def move_to(self, loc):
        try:
            element = self.find_element(loc)
            self.ac.move_to_element(element).perform()
        except Exception as e:
            self.logger.error(f'Error when move to locator {loc}')
            self.logger.exception(e)
        
    def move_element_by_offset(self, loc, *args):
        try:
            offset_x, offset_y = args
            element = self.find_element(loc)
            self.ac.click_and_hold(element).move_by_offset(offset_x, offset_y).release().perform()
        except Exception as e:
            self.logger.error(f'Error when move to locator {loc} by offset')
            self.logger.exception(e)
