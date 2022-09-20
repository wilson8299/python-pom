import os, sys
from time import sleep
sys.path.append(os.getcwd())
import pytest
from utils.browser import Browser
from pages.iframe_page import IframePage
 
@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

class TestIframe:    
    @pytest.fixture(scope='function', name='iframe_page')
    def set_slider_page(self, browser):
        browser.get('https://the-internet.herokuapp.com/iframe')
        yield IframePage(browser)

    def test_get_iframe_content_and_main(self, iframe_page):
        iframe_page.switch_to_iframe()
        content = iframe_page.get_iframe_content()
        assert content == 'Your content goes here.'

    def test_back_default_content(self, iframe_page):
        iframe_page.switch_to_iframe()
        iframe_page.switch_to_default_content()
        content = iframe_page.get_header_content()
        assert content == 'An iFrame containing the TinyMCE WYSIWYG Editor'

if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])