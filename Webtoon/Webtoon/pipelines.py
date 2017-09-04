# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WebtoonPipeline(object):
    files = {}

    def __init__(self):
        global files
        files = {}

    def process_item(self, item, spider):
        global files
        if item['name'] in files:
            files[item['name']]+=item['title']
        else:
            files[item['name']] = item['title']
        return item

    def close_spider(self, spider):
        with open("text.txt",'w') as f:
            for name in files.keys():
                try:
                    f.write('\n\t'+name.strip()+'\n\n')
                except:
                    pass
                for title in files[name]:
                    try:
                        f.write(title+'\n')
                    except:
                        pass