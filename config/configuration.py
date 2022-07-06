import os
import datetime

class Global:
    TEST_TITLE = ''
    PROJECT_ROOT_DIR = file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = PROJECT_ROOT_DIR + '/logs/'
    REOPRT_DIR = PROJECT_ROOT_DIR + '/reports/'
    DATA_DIR = PROJECT_ROOT_DIR + '/data/'
    IMAGE_DIR = REOPRT_DIR + '/images/'
    BROWSER = 'chrome'
    DATETIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %M-%H-%S")