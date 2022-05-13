import time
from urllib import request
import pandas
from bs4 import BeautifulSoup as BS
import re
import csv

start_time = time.time()

#### Page limiter and initial URL ####

page_limit = 10
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

for i in links:
    print(i)


#### check how many pages of definitions each word has and put them in a list ####

last_pages = []
j = 0
for link in links:
    j = j+1
    print('word' + str(j))
    url_3 = link
    html_3 = request.urlopen(url_3)
    bs_3 = BS(html_3.read(), 'html.parser')

    try:
        last_page = bs_3.find('a', string=re.compile('Last')).get('href')
        last_pages.append(url + last_page)
    except:
        last_pages.append(link + '&page=1')

for k in last_pages:
    print(k)

#### make a dataframe with links to words and their last pages ####

df = pandas.DataFrame(links, columns=['links'])

print(df)

df['last pages'] = last_pages

#print(df)
print(df.to_string())

df.to_csv('links.csv', index=False, encoding='utf-8')

#### Loop to open each link and find the number of entries, author and date of entry ####

date_list = []
author_list = []

limit = 'http://urbandictionary.com/define.php?term=YSL&page=3'
x = 1
url_5 = 'http://urbandictionary.com/define.php?term=YSL&page='+ str(x)

while url_5 != limit:
    html_5 = request.urlopen(url_5)
    bs_5 = BS(html_5.read(), 'html.parser')

    authors = bs_5.find_all('a', {'class': 'text-denim dark:text-fluorescent hover:text-limon-lime'}, href=re.compile('^/author.*'))
    dates = bs_5.find_all('div', {'class':'contributor font-bold'})

    for author in authors:
        author_list.append(author.get_text())

    for date in dates:
        d = str(date).split('</',2)
        date_list.append(str(d[1])[3:])

    x = x+1
    url_2 = 'http://urbandictionary.com/define.php?term=YSL&page=' + str(x)


df = pandas.DataFrame(author_list, columns=['authors'])
df['dates'] = date_list

print(df.to_string())

"""for row in df.index:

    limit = df['last pages'][row]
    z = 0
    url_4 = df['links'][row] + '&page=' + str(z)

    while url_4 != limit:

        html_4 = request.urlopen(url_4)
        bs_4 = BS(html_4.read(), 'html.parser')

        authors = bs_4.find_all('a', {'class':'text-denim dark:text-fluorescent hover:text-limon-lime'},  string=re.compile('.'))
        print(authors)

        z = z+1
        url_4 = df['links'][row] + '&page=' + str(z)
"""

#### check how long the script took to execute ####
print("--- Execution time: %s seconds ---" % (time.time() - start_time))
