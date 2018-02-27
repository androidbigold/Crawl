# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class CrawlPipeline(object):
    def __init__(self):
        self.file = codecs.open('F:\\PycharmProjects\\Crawl\\data.json', mode='w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, indent=0) + "\n$\n"
        self.file.write(line)

        return item
