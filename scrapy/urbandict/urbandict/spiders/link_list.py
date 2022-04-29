# -*- coding: utf-8 -*-
import scrapy
import re

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'link_list'
    allowed_domains = ['https://www.urbandictionary.com/']
    try:
        start_urls = ['https://www.urbandictionary.com/?page=1']
    except:
        start_urls = []

    def parse(self, response):
        xpath = '//a[text()="Last »"]//@href'
        selection = response.xpath(xpath)

        text = selection.get()
        pages = re.findall('(\d+)',text)
        print(int(pages[0]))

        for s in range(1,int(pages[0])+1):
            l = Link()
            l['link'] = 'https://www.urbandictionary.com/?page=' + str(s)
            yield l