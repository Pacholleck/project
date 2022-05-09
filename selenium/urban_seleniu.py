limiter=False
global counter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from os import path as pth
import time
import re

### settings ##########

custom_limit=20

word_pages=1

wait_time=2

#######################


#get list of the pages to scrap
def get_wordlinks(limit=word_pages):
    words=[]
    for i in range(1,limit+1):
        url=f'http://urbandictionary.com?page={i}'
        driver.get(url)
        time.sleep(wait_time)
        #try:
        xpath='//h1/a[contains(@href,"define.php?term=")]'
        words_temp=([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH,xpath)])
        words.extend(words_temp)
        #except:
            #words=words.append([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH,"//h1/a")])
    return(words)


########limiter function#############

if limiter==True:
    counter_limit=100
else:
    counter_limit=custom_limit

try:
    # setup driver
    dname = pth.dirname(__file__)
    lpath = '/chromedriver101/chromedriver.exe'
    # Init:
    gecko_path = dname + lpath
    print(gecko_path)
    ser = Service(gecko_path)
    options = webdriver.chrome.options.Options()
    options.headless = False
    driver = webdriver.Chrome(options=options, service=ser)

    url = 'http://urbandictionary.com'

except:

    #setup driver in case chrome is in version 102
    dname=pth.dirname(__file__)
    lpath='/chromedriver/chromedriver.exe'
    # Init:
    gecko_path = dname + lpath
    print(gecko_path)
    ser = Service(gecko_path)
    options = webdriver.chrome.options.Options()
    options.headless = False
    driver = webdriver.Chrome(options = options, service=ser)

    url = 'http://urbandictionary.com'




counter=0

wordlist=get_wordlinks()


print(len(wordlist))
output_table={name}
for link in wordlist:

    xpath = '//a[text()="Last »"]'
    last_number = ([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH, xpath)])

    if last_number is None:
        getpagecontent(output_table)
    else:
        pages = re.findall('(\d+)', text)
        for s in range(1, int(pages[0]) + 1):
            url2= f'{url}&page={s}
            getpagecontent(output_table)




    driver.get(link)



driver.close()