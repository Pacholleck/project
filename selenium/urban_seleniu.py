from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Init:
gecko_path = '/geckodriver/geckodriver.exe'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)