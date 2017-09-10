# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    year = scrapy.Field()
    hum = scrapy.Field()
    raf = scrapy.Field()
    tmi = scrapy.Field()
    tav = scrapy.Field()
    tmx = scrapy.Field()
    pass
