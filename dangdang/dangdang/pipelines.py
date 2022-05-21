# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from dangdang.items import DangdangItem

class DangdangPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1',27017)
        self.conn = self.client['dddd']['ddd']
    def process_item(self, item, spider):
        if isinstance(item,DangdangItem):
            self.conn.insert_one(dict(item))
        return item
