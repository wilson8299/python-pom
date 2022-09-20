import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FileUploadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.select_file_input = By.ID, 'file-upload'
        self.upload_input = By.ID, 'file-submit'
        self.drag_drop_upload = By.ID, 'drag-drop-upload'
        self.drag_drop_upload_text = By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div/span'
        self.uploaded_files_text = By.ID, 'uploaded-files'

    def set_select_file_value(self, value):
        self.send_keys(self.select_file_input, value)

    def get_select_file_value(self):
        return self.get_attribute(self.select_file_input, 'value')

    def get_uploaded_files_text(self):
        return self.get_text(self.uploaded_files_text)

    def get_drag_drop_upload_text(self):
        return self.get_text(self.drag_drop_upload_text)

    def get_drag_drop_upload_element(self):
        return self.find_element(self.drag_drop_upload)

    def click_select_file_input(self):
        self.left_click(self.select_file_input)

    def click_drag_drop_upload(self):
        self.click(self.drag_drop_upload)

    def click_upload(self):
        self.click(self.upload_input)
