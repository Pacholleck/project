# -*- coding: utf-8 -*-
# Import libraries
import scrapy
import re

class Link(scrapy.Item):
    # Set up expected output
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    # For each word, get the maximum number of pages

    limiter = True # Limits the pages if true
    limit = 100 # Set limit of pages to scrap

    # Initialize Spider
    name = 'links_words'

    # Pages to scrap
    allowed_domains = ['https://www.urbandictionary.com/']

    if limiter == True:
        try:
            with open("links.csv", "rt") as f:
                start_urls = [url.strip() for url in f.readlines()][1:limit]
        except:
            start_urls = []
    else:
        try:
            with open("links.csv", "rt") as f:
                start_urls = [url.strip() for url in f.readlines()][1:]
        except:
            start_urls = []
    

    def parse(self, response):
        # Get last link to last page
        xpath = '//a[text()="Last »"]//@href'
        selection = response.xpath(xpath)
        text = selection.get()
        
        if text is None:
            # if there is no link to last page (only one page for this definition)
            name_xpath = response.xpath('//h1/a[re:test(@href, "/define.*")]/@href').get() # Get name of word
            l = Link()
            l['link'] = 'https://www.urbandictionary.com'+ name_xpath # generate link
            yield l
        else:
            # if there are several pages per definition
            pages = re.findall('(\d+)',text) # extract from last link number
            name = re.findall('(\D+)',text) # extract from last link word
            for s in range(1,int(pages[0])+1):
                # Generate for each page till the last page a link
                l = Link()
                l['link'] = 'https://www.urbandictionary.com'+ name[0] + str(s)
                yield l