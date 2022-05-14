import pandas as pd

limit_pages = True
import os

os.system('pip install pandas')
os.system('pip install bs4')

import time
from urllib import request
import pandas
from bs4 import BeautifulSoup as BS
import re
import csv

start_time = time.time()

#### empty final data frame ####
# dfObj = pd.DataFrame(columns=['User_ID', 'UserName', 'Action'])
df1 = pandas.DataFrame(columns=['word', 'author', 'date'])

#### Page limiter and initial URL ####

page_limit = 10

if limit_pages == True:
    page_limit_ALL = 90
else:
    page_limit_ALL = 2

url = 'http://urbandictionary.com'
links = []

#### The ugliest link finder imaginable, like seriously don't look at it, but it works ####

for i in range(1, int(page_limit)+1):
    #print('page' + str(i))
    url_2 = 'http://urbandictionary.com/?page=' + str(i)
    html_2 = request.urlopen(url_2)
    bs_2 = BS(html_2.read(), 'html.parser')

    for a in bs_2.find_all('a', {'class':'word text-denim font-bold font-serif dark:text-fluorescent break-words text-3xl md:text-[2.75rem] md:leading-10'}, href=re.compile('define.*')):
        x = url + a['href']
        links.append(x)
        #print(x)


#### Loop to open each link and find the number of entries, author and date of entry ####

words = []
date_list = []
author_list = []
counter = 1

for link in links:

    if counter <= page_limit_ALL:

        url_3 = link
        html_3 = request.urlopen(url_3)
        bs_3 = BS(html_3.read(), 'html.parser')

        try:
            last_page = bs_3.find('a', string=re.compile('Last')).get('href')
        except:
            last_page = link + '&page=1'


        limit_2 = last_page.split('page=', 1)
        limit_3 = limit_2[1]

        #print(limit_3[0])

        #print("1")

        for x in range(1,int(limit_3)+1):

            if counter <= page_limit_ALL:
                print(f'Please wait, current progress: {(counter+10)*100/(page_limit_ALL+10)}%')
                url_5 = link + '&page=' + str(x)
                html_5 = request.urlopen(url_5)
                bs_5 = BS(html_5.read(), 'html.parser')
                divs = bs_5.find_all('div',{'class': 'p-5 md:p-8'})

                for div in divs:


                    #print("2")
                    word = div.findNext('a',{'class': 'word text-denim font-bold font-serif dark:text-fluorescent break-words text-3xl md:text-[2.75rem] md:leading-10'}).get_text()
                    authors = div.findNext('a', {'class': 'text-denim dark:text-fluorescent hover:text-limon-lime'}, href=re.compile('^/author.*')).get_text()
                    dates = div.findNext('div', {'class': 'contributor font-bold'})
                    #print(str(dates))



                    l4d = str(dates).split('</',2)
                    dates = str(l4d[1])[3:]



                    d = {'word': word, 'author': authors, 'date': dates}
                    series=pd.Series(data=d,index=d.keys()).to_frame().T
                    df1=pd.concat([series,df1])
                    #df1 = df1.append(d, ignore_index=True)

                counter = counter + 1

            else:
                break
        #print(counter)
    else:
        break

        #url_5 = 'http://urbandictionary.com/define.php?term=YSL&page=' + str(x)




#print(df1.to_string())



#### check how long the script took to execute ####
print(" ")
print("--- Execution time: %s seconds ---" % (time.time() - start_time))

df1.to_csv('outputSoup.csv', index=False, encoding='utf-8')
