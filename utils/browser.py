import os, sys
sys.path.append(os.getcwd())
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from utils.logger import Logger
from config.configuration import Global

class Browser:
    def __init__(self):
        self.logger = Logger('browser')

    def open_browser(self):
        self.logger.info(f'Selected {Global.BROWSER} browser.')

        if Global.BROWSER == 'chrome':
            options = Options()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            self.logger.info('Starting chrome browser.')
        elif Global.BROWSER == 'firefox':
            self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            self.logger.info('Starting firefox browser.')
        elif Global.BROWSER == 'edge':
            self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
            self.logger.info('Starting edge browser.')
        elif Global.BROWSER == 'ie':
            self.driver = webdriver.Ie(service=Service(IEDriverManager().install()))
            self.logger.info('Starting ie browser.')

        return self.driver

    def close_browser(self):
        self.logger.info('Close chrome browser.')
        self.driver.close()
        self.driver.quit()