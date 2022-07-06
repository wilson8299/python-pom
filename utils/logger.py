import os, sys
sys.path.append(os.getcwd())
import logging
from config.configuration import Global

class Logger(logging.Logger):
    def __init__(self, logger, logger_level = logging.DEBUG) -> None:
        super().__init__(logger)
        formatter = logging.Formatter('[%(asctime)s] %(name)s - %(funcName)s - %(levelname)s - %(message)s')
        file_name = Global.LOG_DIR + Global.DATETIME_NOW + '_log.log'
        file_handler = logging.FileHandler(file_name, encoding="utf-8-sig")
        file_handler.setLevel(logger_level)
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)