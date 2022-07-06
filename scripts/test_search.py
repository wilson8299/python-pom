import os, sys
sys.path.append(os.getcwd())
import pytest
from utils.browser import Browser
from pages.search_page import SearchPage
from selenium.webdriver.common.keys import Keys
from utils.read_yaml import read_yaml

@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

@pytest.mark.usefixtures('browser')
class TestSearch:
    
    @pytest.fixture(scope='function', name='search_page')
    def set_search_page(self, browser):
        browser.get('https://www.google.com')
        yield SearchPage(browser)

    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.parametrize('content', read_yaml('search_data')['search_content'])
    def test_search_content_use_enter(self, search_page, content):
        search_page.input_content(content)
        search_page.input_content(Keys.ENTER)
        assert content in search_page.get_title()

    def test_search_content_use_click(self, search_page):
        search_page.input_content('Edge')
        search_page.focus_searchbar()
        search_page.click_search_button()
        assert 'Edge' in search_page.get_title()

    def test_search_page_screenshot(self, search_page):
        search_page.page_screenshot()

if __name__ == '__main__':
    pytest.main(["-v"])