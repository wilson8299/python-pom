import os, sys
sys.path.append(os.getcwd())
import yaml
from config.configuration import Global

def read_yaml(file_name):
    with open(f'{Global.DATA_DIR}{file_name}.yml', 'r') as f:
        return yaml.load(f, Loader=yaml.CLoader)