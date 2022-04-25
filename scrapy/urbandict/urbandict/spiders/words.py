# -*- coding: utf-8 -*-
from multiprocessing import Condition
from operator import lshift
import scrapy

class Words(scrapy.Item):
    name        = scrapy.Field()
    author      = scrapy.Field()
#    upvotes     = scrapy.Field()
#    downvotes   = scrapy.Field() 
    date        = scrapy.Field()
    # meaning     = scrapy.Field()


class LinksSpider(scrapy.Spider):
    name = 'words'
    allowed_domains = ['https://www.urbandictionary.com/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:3]
    except:
        start_urls = []

    def parse(self, response):
        p = Words()

        name_xpath          = '//h1/a[re:test(@href, "/define.*")]/text()'
        author_xpath         = '//a[re:test(@href, "/author.*")]/text()'
        #upvotes_xpath          = '//div[@data-direction="up"]/span'
        #downvotes_xpath      = '//div[@data-direction="down"]/span/text()'
        date_xpath         = '//a[re:test(@href, "/author.*")]/following-sibling::text()'
        # meaning_xpath         = '//div[@aria-label="Piętro"]/div[2]/div/text()'    
       
        p['name']       = response.xpath(name_xpath).get()
        p['author']     = response.xpath(author_xpath).get()
        #p['upvotes']    = response.xpath(upvotes_xpath).get()
        #p['downvotes']  = response.xpath(downvotes_xpath).getall()
        p['date']       = response.xpath(date_xpath).get()

        


        yield p

