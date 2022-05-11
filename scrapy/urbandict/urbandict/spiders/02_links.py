# -*- coding: utf-8 -*-
# Import libraries
import scrapy

class Link(scrapy.Item):
    # Set up expected output
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    # For each page, extract the link to the word

    limiter = True # Limits the pages if true
    limit = 100 # Set limit of pages to scrap
    
    # Initialize Spider
    name = 'links'

    # Pages to scrap
    allowed_domains = ['https://www.urbandictionary.com/']
    
    if limiter == True:
        try:
            # Scrap from all the different pages either to max or to limit
            with open("link_list.csv", "rt") as f:
                start_urls = [url.strip() for url in f.readlines()][1:limit]
        except:
            start_urls = []
    else:
        try:
            # Scrap from all the different pages either to max or to limit
            with open("link_list.csv", "rt") as f:
                start_urls = [url.strip() for url in f.readlines()][1:]
        except:
            start_urls = []


    def parse(self, response):
        #Extract link to definitions
        xpath = '//h1/a[re:test(@href, "/define.*")]//@href' 
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.urbandictionary.com' + s.get()
            yield l