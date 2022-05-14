# Webscraping - [urbandictionary.com](https://www.urbandictionary.com/)

## Run Beautiful Soup

1. Run main.py in soup folder
2. The required packages should install automatically
3. Progress percentage is displayed during the run
4. At finish program displays run time
5. After the program finishes output is saved in outputSoup.csv

## Run Scrapy
To run scrapy, use the following commands in this order: 
1. `scrapy crawl link_list -O link_list.csv`
2. `scrapy crawl links -O links.csv`
3. `scrapy crawl links_words -O links_words.csv`
4. `scrapy crawl words -O words.csv`

If you wish to remove or change the limit of the maximum number of pages to scrap, please set `limiter` to "False" 
or modify `limit` in the .py-files under /scrapy/urbandict/urbandict/spider.

Please make sure to have [Scrapy](https://docs.scrapy.org/en/latest/) installed properly.

## Run Selenium

1. Run urban_seleniu.py in the selenium folder
2. The required packages should install automatically
3. Progress is displayed during the run
4. After the program finishes output is saved in output.csv
