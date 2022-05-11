# webscaping_project

## Run Beautiful Soup

## Run Scrapy
To run scrapy, use the following commands in this order: 
1. `scrapy crawl link_list -O link_list.csv`
2. `scrapy crawl links -O links.csv`
3. `scrapy crawl links_words -O links_words.csv`
4. `scrapy crawl words -O words.csv`

If you wish to remove or change the limit of the maximum number of pages to scrap, please set `limiter` to "False" 
or modify `limit` in the .py-files under /scrapy/urbandict/urbandict/spider.

## Run Selenium
