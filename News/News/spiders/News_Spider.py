# -*- coding: utf-8 -*-

import scrapy
from News.items import NewsItem

class Crawling_Spider(scrapy.Spider):
    name = "news"
    start_urls=[
        "http://media.daum.net/society/"
    ]

    def parse(self,response):
        for href in response.xpath('//*[@id="mArticle"]/ul//li/div/strong/a/@href').extract():
            yield scrapy.Request(href, callback = self.parse_list)

    def parse_list(self,response):
        item = NewsItem()

        for href in response.xpath('//*[@id="harmonyContainer"]/section//p/text()').extract():
            item['string']=href
            yield item
