# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'links'
    allowed_domains = ['https://www.urbandictionary.com/']
    try:
        start_urls = ['https://www.urbandictionary.com/?page='+str(i) for i in range(1,50)]
    except:
        start_urls = []

    def parse(self, response):
        xpath = '//h1/a[re:test(@href, "/define.*")]//@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.urbandictionary.com' + s.get()
            yield l