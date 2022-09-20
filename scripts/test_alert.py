import os, sys
sys.path.append(os.getcwd())
import pytest
from utils.browser import Browser
from pages.alert_page import AlertPage
 
@pytest.fixture(scope='class', name='browser')
def set_browser():
    browser = Browser()
    driver = browser.open_browser()
    yield driver
    browser.close_browser()

class TestAlert:    
    @pytest.fixture(scope='function', name='alert_page')
    def set_slider_page(self, browser):
        browser.get('https://the-internet.herokuapp.com/javascript_alerts')
        yield AlertPage(browser)

    def test_alert(self, alert_page):
        alert_page.click_alert_button()
        alert_page.accept_alert()
        content = alert_page.get_result_content()
        assert content == 'You successfully clicked an alert'

    def test_confirm_ok(self, alert_page):
        alert_page.click_confirm_button()
        alert_page.accept_alert()
        content = alert_page.get_result_content()
        assert content == 'You clicked: Ok'

    def test_confirm_cancel(self, alert_page):
        alert_page.click_confirm_button()
        alert_page.dismiss_alert()
        content = alert_page.get_result_content()
        assert content == 'You clicked: Cancel'

    def test_prompt_message(self, alert_page):
        expect = 'prompt'
        alert_page.click_prompt_button()
        alert_page.type_alert_message(expect)
        alert_page.accept_alert()
        content = alert_page.get_result_content()
        assert content == 'You entered: ' + expect

if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])