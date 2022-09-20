import os, sys
sys.path.append(os.getcwd())
import pytest
from utils.browser import Browser
from pages.blank_page import BlankPage
 
@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

class TestBlank:
    @pytest.fixture(scope='function', name='blank_page')
    def set_slider_page(self, browser):
        browser.get('https://the-internet.herokuapp.com/windows')
        yield BlankPage(browser)

    def test_open_correct_page(self, blank_page):
        blank_page.click_link()
        header = blank_page.get_new_page_header()
        assert header == 'New Window'

if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])