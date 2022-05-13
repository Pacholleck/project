from urllib import request
import pandas
from bs4 import BeautifulSoup as BS
import re
import csv

date_list = []
author_list = []

limit = 'http://urbandictionary.com/define.php?term=YSL&page=3'
x = 1
url_2 = 'http://urbandictionary.com/define.php?term=YSL&page='+ str(x)

html_2 = request.urlopen(url_2)
bs_2 = BS(html_2.read(), 'html.parser')

authors = bs_2.find_all('a', {'class': 'text-denim dark:text-fluorescent hover:text-limon-lime'}, href=re.compile('^/author.*'))
dates = bs_2.find_all('div', {'class':'contributor font-bold'})

for author in authors:
    author_list.append(author.get_text())

for date in dates:
    d = str(date).split('</',2)
    date_list.append(str(d[1])[3:20])


df = pandas.DataFrame(author_list, columns=['authors'])
df['dates'] = date_list

print(df.to_string())
