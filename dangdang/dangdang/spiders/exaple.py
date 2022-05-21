import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy_redis.dupefilter import RFPDupeFilter
from scrapy_redis.scheduler import Scheduler
from scrapy_redis.queue import PriorityQueue,LifoQueue,FifoQueue
from scrapy import cmdline
from dangdang.items import DangdangItem

class ExapleSpider(RedisSpider):
    name = 'exaple'
    # allowed_domains = ['baidu.com']
    # start_urls = ['http://baidu.com/']
    redis_key = 'url:start'

    rule = {
        'index_data':'//ul[@class="bigimg"]/li',
        'title':'./p[@class="name"]/a/@title',
        'price':'.//p[@class="price"]/span[@class="search_now_price"]/text()',
        'author':'./p[@class="search_book_author"]/span/a[2]/@title',
        'page': '//div[@class="paging"]/ul/li[@class="next"]/a/@href'
    }

    def parse(self, response):
        datas = response.xpath(self.rule['index_data'])
        for data in datas:
            item = DangdangItem()
            item['title'] = data.xpath(self.rule['title']).extract_first()
            item['price'] = data.xpath(self.rule['price']).extract_first()
            item['author'] = data.xpath(self.rule['author']).extract_first()
            yield item
        base_url = 'http://search.dangdang.com'
        page = response.xpath(self.rule['page']).extract_first()
        yield scrapy.Request(url=base_url + page,callback=self.parse)


if __name__ == '__main__':
    cmdline.execute('scrapy crawl exaple'.split())