# -*- coding: utf-8 -*-
import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

def Make_2d_array(arr):
    result=[]
    month=13
    inner_array=[]
    index=0
    for i in arr:
        index += 1
        if index==1:
            continue
        inner_array.append(i)
        if index==month:
            result.append(inner_array)
            inner_array=[]
            index=0
    return result


class WeatherPipeline(object):
    def __init__(self):
        global csv_file
        global csv_writer
        csv_file = open('data.csv','w',newline="")
        csv_writer = csv.writer(csv_file)
        category = ["지점","일시","습도","강수량","최저온도","평균온도","최고온도"]
        csv_writer.writerow(category)

    def process_item(self, item, spider):
        hum = Make_2d_array(item['hum'])
        raf = Make_2d_array(item['raf'])
        tmi = Make_2d_array(item['tmi'])
        tmx = Make_2d_array(item['tmx'])
        tav = Make_2d_array(item['tav'])

        for i in range(12):
            for j in range(31):
                if hum[j][i]==' ':
                    continue
                csv_writer.writerow(["108",item['year']+'-'+str(i+1)+'-'+str(j+1),hum[j][i],raf[j][i],tmi[j][i],tmx[j][i],tav[j][i]])

        return item

    def close_spider(self,spider):
        csv_file.close()