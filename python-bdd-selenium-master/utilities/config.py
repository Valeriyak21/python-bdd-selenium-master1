import configparser
import os
import selenium.webdriver as webdriver


class Config(object):
    """
    Config class for storing values from config.ini and browser types.
    """
    browser_types = \
        dict(chrome=webdriver.Chrome, firefox=webdriver.Firefox, ie=webdriver.Ie, phantomjs=webdriver.PhantomJS)
    config = configparser.ConfigParser()
    config.read('config.ini')

    BROWSER = config.get('SELENIUM', 'Browser').lower()
    HIGHLIGHT = config.getboolean('SELENIUM', 'Highlight')
    REUSE = config.getboolean('SELENIUM', 'Reuse')

    APP_URL = config.get('APPLICATION', 'URL')
    APP_URL_1 = config.get('APPLICATION', 'URL_1')

    LOG_DIR = os.path.abspath('logs')
