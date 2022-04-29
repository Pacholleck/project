# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'links'
    allowed_domains = ['https://www.urbandictionary.com/']
    try:
        with open("link_list.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:5]
    except:
        start_urls = []

    def parse(self, response):
        xpath = '//h1/a[re:test(@href, "/define.*")]//@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = 'https://www.urbandictionary.com' + s.get()
            yield l