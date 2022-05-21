# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import pymysql
from xinwen.items import XinwenItem1

class XinwenPipeline:

    def open_spider(self,spider):
        self.client = pymongo.MongoClient()
        self.db = self.client.news

    def process_item(self, item, spider):
        items = dict(item)
        if isinstance(items,dict):
            self.db['xl'].insert_one(items)
            return item
        else:
            return "数据格式不对"

class XinwenPipeline1:

    def open_spider(self,spider):
        data_config = spider.settings['DATA_CONFIG']
        self.conn = pymysql.Connection(**data_config['config'])
        self.cursor = self.conn.cursor()

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self,item,spider):
        if isinstance(item,XinwenItem1):
            try:
                sql = 'insert into xialuo (title,times,info) values (%s,%s,%s)'
                self.cursor.execute(sql,(
                    item['title'],
                    item['times'],
                    item['info']
                ))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print('信息写入错误%s-%s'%(item['url'],e))