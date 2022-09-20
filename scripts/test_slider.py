import os, sys
sys.path.append(os.getcwd())
import pytest
from utils.browser import Browser
from pages.slider_page import SliderPage
 
@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

class TestSlider:    
    @pytest.fixture(scope='function', name='slider_page')
    def set_slider_page(self, browser):
        browser.get('https://the-internet.herokuapp.com/horizontal_slider')
        yield SliderPage(browser)

    def test_slide_slider2five(self, slider_page):
        slider_page.move_slider(129, 0)
        value = slider_page.get_slider_value()
        assert value == str(5)

if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])