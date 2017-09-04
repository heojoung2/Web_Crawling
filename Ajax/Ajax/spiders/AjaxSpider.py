#-*- coding:utf-8 -*-

import scrapy

from selenium import webdriver
from scrapy.selector import Selector
from Ajax.items import AjaxItem

class AjaxSpider(scrapy.Spider):
    name = "ajax"
    allowed_domains = ["blog.daum.net/"]
    start_urls = [
        "http://blog.daum.net/"
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("C:/Users/heo/Desktop/chromedriver.exe")

    def parse(self,response):
        self.browser.get(response.url)
        html = self.browser.find_element_by_xpath("//*[@id='bestMore']")
        item=AjaxItem()

        for i in range(2):
            html.click()

        html=self.browser.find_element_by_xpath("//*").get_attribute('outerHTML')
        selector = Selector(text=html)

        rows=selector.xpath("//*[@id='top_articles']//ul//li//div//a[@class='link_subject']/text()").extract()
        for i in rows:
            item['name']=i
            yield item

        self.browser.close()