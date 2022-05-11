# -*- coding: utf-8 -*-
# Import libraries
from multiprocessing import Condition
from operator import lshift
import scrapy

class Words(scrapy.Item):
    # Set up expected output
    word        = scrapy.Field()
    author      = scrapy.Field()
    date        = scrapy.Field()


class LinksSpider(scrapy.Spider):
    # Use list with all links to each word with its multiple subpages to extract the word, author and date.
    
    limiter = True # Limits the pages if true
    limit = 100 # Set limit of pages to scrap

    # Initialize Spider
    name = 'words'

    # Pages to scrap
    allowed_domains = ['https://www.urbandictionary.com/']
    if limiter == True:
        try:
            with open("links_words.csv", "rt") as f:
                start_urls = [url.strip() for url in f.readlines()][1:limit]
        except:
            start_urls = []
    else:
        try:
            with open("links_words.csv", "rt") as f:
                start_urls = [url.strip() for url in f.readlines()][1:]
        except:
            start_urls = []

    def parse(self, response):
        p = Words()

        name_xpath          = '//h1/a[re:test(@href, "/define.*")]/text()'
        author_xpath         = '//a[re:test(@href, "/author.*")]/text()'
        date_xpath         = '//a[re:test(@href, "/author.*")]/following-sibling::text()'  
       
        word      = response.xpath(name_xpath).getall()
        author     = response.xpath(author_xpath).getall()
        date       = response.xpath(date_xpath).getall()

        for i in range(0,len(word)):
            p['word']       = word[i]
            p['author']     = author[i]
            p['date']       = date[i]

            yield p

