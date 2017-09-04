# -*- coding: utf-8 -*-

import scrapy

from Webtoon.items import WebtoonItem

mylist = []

class WebtoonSpider(scrapy.Spider):
    name = "webtoon"
    allowed_domains = ["comic.naver.com"]
    start_urls=[
        "http://comic.naver.com/webtoon/weekday.nhn"
    ]

    def parse(self, response):
        global mylist

        for href in response.xpath('//div[@class = "list_area daily_all"]//a[@class="title"]/@href').extract():
            url = response.urljoin(href)
            url_utf = url

            if url_utf[:-5] not in mylist:
                mylist.append(url_utf[:-5])
                yield scrapy.Request(url, callback=self.parse_list)

    def parse_list(self,response):
        item = WebtoonItem()

        item['name']=response.xpath('//div[@class="detail"]/h2/text()').extract()[0]
        item['title']=response.xpath('//td[@class="title"]/a/text()').extract()
        yield item

        next_page = response.xpath('//div[@class="page_wrap"]//a[@class="next"]/@href').extract()

        for i in next_page:
            url=response.urljoin(i)
            yield scrapy.Request(url,callback=self.parse_list)
