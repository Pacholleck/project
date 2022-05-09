from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from os import path as pth
import time

dname=pth.dirname(__file__)

# Init:
gecko_path = dname + '/geckodriver/geckodriver.exe'
print(gecko_path)
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)