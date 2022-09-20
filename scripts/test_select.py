import os, sys
sys.path.append(os.getcwd())
import pytest
from utils.browser import Browser
from pages.select_page import SelectPage
 
@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

class TestSelect:    
    @pytest.fixture(scope='function', name='select_page')
    def set_slider_page(self, browser):
        browser.get('https://the-internet.herokuapp.com/dropdown')
        yield SelectPage(browser)

    def test_get_default_text(self, select_page):
        text = select_page.get_select_text()
        assert text == 'Please select an option'

    def test_set_select_option1_by_index(self, select_page):
        select_page.set_select_by_index(1)
        text = select_page.get_select_text()
        assert text == 'Option 1'

if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])