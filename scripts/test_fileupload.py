import os, sys
from time import sleep
sys.path.append(os.getcwd())
import pytest
import pyautogui
from utils.browser import Browser
from pages.fileupload_page import FileUploadPage
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

class TestFileUpload:
    file_abspath = __file__
    file_name = os.path.basename(__file__)
    
    @pytest.fixture(scope='function', name='file_upload_page')
    def set_file_upload_page(self, browser):
        browser.get('https://the-internet.herokuapp.com/upload')
        yield FileUploadPage(browser)

    def test_set_select_input_value_use_sendkeys(self, file_upload_page):
        file_upload_page.set_select_file_value(self.file_abspath)
        value = file_upload_page.get_select_file_value()
        assert self.file_name in value

    def test_set_select_input_use_window(self, file_upload_page):
        file_upload_page.click_select_file_input()
        sleep(1)
        pyautogui.write(self.file_abspath)
        pyautogui.press('enter', 2)
        value = file_upload_page.get_select_file_value()
        assert self.file_name in value

    def test_submit(self, file_upload_page):
        file_upload_page.set_select_file_value(self.file_abspath)
        file_upload_page.click_upload()
        text = file_upload_page.get_uploaded_files_text()
        assert self.file_name == text

    def test_set_drag_drop_upload_use_window(self, file_upload_page):
        file_upload_page.click_drag_drop_upload()
        sleep(1)
        pyautogui.write(self.file_abspath)
        pyautogui.press('enter', 2)
        text = file_upload_page.get_drag_drop_upload_text()
        assert self.file_name in text

if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])