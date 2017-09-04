# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):
    def __init__(self):
        global outfile
        outfile = open('news_text.txt','w')

    def process_item(self, item, spider):
        string=item['string'].strip()
        if not (len(string)==0 or len(string)==1) :
            outfile.write(string+'\n')
        return item

    def close_spider(self,spider):
        outfile.close()
