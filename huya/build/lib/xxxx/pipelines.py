# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs

from itemadapter import ItemAdapter
import json
import os

class XxxxPipeline:

    def open_spider(self,spider):
        self.file = codecs.open('data2.json', 'w+', encoding='UTF-8')
        self.file.write('[\n')
    def close_spider(self,spider):
        self.file.seek(-2, os.SEEK_END)
        self.file.truncate()
        self.file.write('\n]')
        self.file.close()

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(item_json + ',\n')
        return item
