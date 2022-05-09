limiter=False

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from os import path as pth
import time
import re

custom_limit=1

if limiter==True:
    limit=100
else:
    limit=custom_limit

#setup geckodriver
dname=pth.dirname(__file__)
lpath='/geckodriver/geckodriver.exe'
# Init:
gecko_path = dname + lpath
print(gecko_path)
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = True
driver = webdriver.Firefox(options = options, service=ser)


url = 'http://urbandictionary.com'


def get_wordlinks(limit=limit):
    words=[]
    for i in range(1,limit+1):
        url=f'http://urbandictionary.com?page={i}'
        driver.get(url)
        try:
            words_temp=([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH,"//h1/a[matches(@href,'/define*')]")])
            words.extend(words_temp)
        except:
            words=words.append([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH,"//h1/a")])
    return(words)


    driver.close()

wordlist=get_wordlinks()
print(wordlist)