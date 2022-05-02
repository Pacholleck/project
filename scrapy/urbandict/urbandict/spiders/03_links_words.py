# -*- coding: utf-8 -*-
import scrapy
import re

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'links_words'
    allowed_domains = ['https://www.urbandictionary.com/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        xpath = '//a[text()="Last »"]//@href'
        selection = response.xpath(xpath)
        text = selection.get()
        


        if text is None:
            name_xpath = response.xpath('//h1/a[re:test(@href, "/define.*")]/@href').get()
            print(name_xpath)
            l = Link()
            l['link'] = 'https://www.urbandictionary.com'+ name_xpath
            yield l
        else:
            pages = re.findall('(\d+)',text)
            name = re.findall('(\D+)',text)
            for s in range(1,int(pages[0])+1):
                l = Link()
                l['link'] = 'https://www.urbandictionary.com'+ name[0] + str(s)
                yield l