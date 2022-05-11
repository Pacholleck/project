limiter = True
global counter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from os import path as pth
import time
import re
import pandas as pd

### settings ##########

custom_limit = 400

word_pages = 10

wait_time = 1


# get list of the pages to scrap
def get_wordlinks(limit=word_pages):
    words = []
    for i in range(1, limit + 1):
        url = f'http://urbandictionary.com?page={i}'
        driver.get(url)
        time.sleep(wait_time)
        # try:
        xpath = '//h1/a[contains(@href,"define.php?term=")]'
        words_temp = ([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH, xpath)])
        words.extend(words_temp)
        # except:
        # words=words.append([my_elem.get_attribute("href") for my_elem in driver.find_elements(By.XPATH,"//h1/a")])
    return (words)


def getpagecontent(url):
    #dict = {'author': [], 'date': [], 'word': []}
    df=pd.DataFrame({'word': [],'author': [],'date': []})
    driver.get(url)
    time.sleep(wait_time)
    # auth_xpath="//div[contains(@class,'contributor')]/a[contains(@href,'.php?author=')]"
    #auth_xpath = "//div[contains(@class,'contributor')]"
    div_xpath='//div[contains(@class,"p-5 md:p-8")]'
    authors = driver.find_elements(By.XPATH, div_xpath)
    for div in authors:
        d=div.find_element(By.XPATH,".//div[contains(@class,'contributor')]")
        d=d.get_attribute('innerHTML').split('</a>')[1].strip()
        a=div.find_element(By.XPATH,".//div/a[contains(@href,'.php?author=')]").get_attribute('text')
        h = div.find_element(By.XPATH, "./div/h1/a[contains(@href,'define')]").get_attribute('text')
        dict={'word':h,'author':a,'date': d}
        df=df.append(dict,ignore_index=True)
    return (df)



######## limiter function #############


if limiter == True:
    counter_limit = 90
else:
    counter_limit = custom_limit

############ setup driver #############
try:

    dname = pth.dirname(__file__)
    lpath = '/geckodriver/geckodriver.exe'
    # Init:
    gecko_path = dname + lpath
    print(gecko_path)
    ser = Service(gecko_path)
    options = webdriver.firefox.options.Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, service=ser)

    url = 'http://urbandictionary.com'


except:

    # setup driver in case chrome is in version 102
    dname = pth.dirname(__file__)
    lpath = '/chromedriver/chromedriver.exe'
    # Init:
    gecko_path = dname + lpath
    ser = Service(gecko_path)
    options = webdriver.chrome.options.Options()
    options.headless = False
    driver = webdriver.Chrome(options=options, service=ser)

    url = 'http://urbandictionary.com'

#### starting value of page counter ############
counter = 1

###### list of links to words from main page ##########
wordlist = get_wordlinks()

##### create output dataframe #########
output_frame = pd.DataFrame({'word': [],'author': [],'date': []})

#### go through link of every word from the main page ########
for link in wordlist:

    ####### check whether the limit of the pages is reached ########
    if counter <= counter_limit:
        driver.get(link)

        ####### XPath to search for the "last" button ######
        xpath = '//a[text()="Last »"]'

        ####### get number of the last page, or return None if there isn't one ############
        try:
            my_elem = driver.find_element(By.XPATH, xpath)
            last_number = my_elem.get_attribute("href")
        except:
            last_number = None

        ############if there is no last button then there is only one page. scrap data from the page and increase the counter for page limit##############
        if last_number is None:
            fdf=getpagecontent(link)
            counter = counter + 1
            output_frame=pd.concat([output_frame,fdf])

        ########## if there is a last page number find it and loop through all pages until the last increasing counter for each page scraped###########
        else:
            pages = re.findall('(\d+)', last_number)
            for s in range(1, int(pages[0]) + 1):
                url2 = f'{link}&page={s}'
                fdf=getpagecontent(url2)
                counter = counter + 1
                output_frame=pd.concat([output_frame,fdf])
    ############ upon reaching page limit return information and break loop############
    else:
        print("page limit reached")
        break


output_frame.to_csv("output.csv")
######## close connection ##########
driver.close()
