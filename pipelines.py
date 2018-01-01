# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class M80SPipeline(object):
    def process_item(self, item, spider):
        try:
            rate = float(item['rate'][0])
            durl = item['downloadurl'][0]
            #print('\n-----------------------'+durl+'-----------------\n')
            if (rate>=6.5) & (len(durl) > 20):
                #print('\n----ITEM---IS----OK------------'+item['rate'][0]+'-----------------\n')
                return item
            else:
                #print('\n\nitem has no download url and rate is less than [6.5]\n\n')
                pass
        except:
            pass
