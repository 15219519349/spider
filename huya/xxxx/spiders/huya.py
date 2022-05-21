import scrapy
from scrapy import cmdline
from scrapy.utils import log
from xxxx.items import XxxxItem
page = 1
class HuyaSpider(scrapy.Spider):
    name = 'huya'
    allowed_domains = ['huya.com']
    # start_urls = ['http://huya.com/']

    def start_requests(self):
        start_urls = f'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&page={page}'
        yield scrapy.Request(url=start_urls,meta={'page':page})


    def parse(self, response):
        item = XxxxItem()
        log.logger.warning(f'正在爬取第{response.meta.get("page")}页数据')
        totalpage = response.json().get('data').get('totalPage')
        datas = response.json().get('data').get('datas')
        print(datas)
        for data in datas:
            item['name'] = data.get('roomName')
            yield item
        global page
        page += 1
        if page <= totalpage:
            start_urls = f'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&page={page}'
            yield scrapy.Request(url=start_urls, meta={'page': page},dont_filter=True)


if __name__ == '__main__':
    cmdline.execute('scrapy crawl huya'.split())
