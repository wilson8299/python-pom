import os, sys
sys.path.append(os.getcwd())
import pytest
import os
from config.configuration import Global
from utils.logger import Logger

def pytest_addoption(parser):
    group = parser.getgroup("custom-report")
    group.addoption("--browser")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = Global.REOPRT_DIR + Global.DATETIME_NOW + '_report.html'

    browser = config.getoption("--browser")
    if browser:
        Global.BROWSER = browser.lower()

@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    logger = Logger('Test')
    logger.info(f'Execute {request.node.nodeid}')

def pytest_html_report_title(report):
    report.title = Global.TEST_TITLE