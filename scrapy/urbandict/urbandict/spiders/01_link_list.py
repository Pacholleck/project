# -*- coding: utf-8 -*-
# Import libraries
import scrapy
import re

class Link(scrapy.Item):
    # Set up expected output
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    # Extract the maximum number of pages and generate links to each page

    # Initialize Spider
    name = 'link_list'

    # Pages to scrap
    allowed_domains = ['https://www.urbandictionary.com/']
    try:
        # Scrap the startpage
        start_urls = ['https://www.urbandictionary.com/?page=1']
    except:
        start_urls = []

    def parse(self, response):
        # Get link to last page
        xpath = '//a[text()="Last »"]//@href'
        selection = response.xpath(xpath)
        text = selection.get()
        # Extract number of last page
        pages = re.findall('(\d+)',text)

        for s in range(1,int(pages[0])+1):
            #Generate links up to last page
            l = Link()
            l['link'] = 'https://www.urbandictionary.com/?page=' + str(s)
            yield l