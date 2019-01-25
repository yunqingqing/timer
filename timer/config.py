import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(BASE_DIR, 'timer.ini'))


class LazySettings:
    ''' 配置类。默认使用timer.ini文件 '''
    def __getattr__(self, name):
        if name in CONFIG:
            return CONFIG[name]


settings = LazySettings()
