# -*- coding: utf-8 -*-

import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from Weather.items import WeatherItem
import time

class Crawling_Spider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["www.kma.go.kr/"]
    start_urls=[
        "http://www.kma.go.kr/weather/climate/past_table.jsp?stn=108&yy=2011&obs=07&x=29&y=11"
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome("C:/Users/heo/Desktop/chromedriver.exe")


    def parse(self,response):
        item = WeatherItem()
        year_list = [i for i in range(7, 2,-1)]
        category_num_list = [7,4,2,3,1]
        category_list = ['hum', 'raf', 'tmi', 'tav', 'tmx']

        for year in year_list:
            self.browser.get(response.url)
            html = self.browser.find_element_by_xpath('//*[@id="observation_select2"]/option[' + str(year) + ']')
            html.click()
            time.sleep(1)
            item['year'] = response.xpath('//*[@id="observation_select2"]/option[' + str(year) + ']/text()').extract()[0]

            for category in category_list:
                item[category]=[]
            category_num=0

            for category in category_num_list:
                html = self.browser.find_element_by_xpath('//*[@id="observation_select3"]/option['+str(category)+']')
                html.click()
                time.sleep(1)

                html = self.browser.find_element_by_xpath('//*[@id="content_weather"]/form/fieldset/input[3]')
                html.click()
                time.sleep(1)

                html = self.browser.find_element_by_xpath("//*").get_attribute('outerHTML')
                selector = Selector(text=html)

                for value in selector.xpath('//*[@id="content_weather"]/table/tbody//tr//td/text()').extract():
                    try:
                        print(value)
                    except:
                        value = ' '
                    item[category_list[category_num]].append(value)
                category_num+=1
            yield item

        self.browser.close()
