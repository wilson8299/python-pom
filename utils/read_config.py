import configparser

class ReadConfig:
    def __init__(self, path) -> None:
        self.conf = configparser.ConfigParser()
        self.conf.read(path, encoding="utf-8-sig")

    def set_value(self, section, name, value):
        self.conf.set(section, name, value)

    def get_value(self, section, name):
        return self.conf.get(section, name)