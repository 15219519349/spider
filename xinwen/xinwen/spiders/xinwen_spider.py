import scrapy
from scrapy import cmdline
from scrapy.utils import log
from xinwen.items import XinwenItem
from urllib.parse import urljoin



class XinwenSpiderSpider(scrapy.Spider):
    name = 'xinwen_spider'
    # allowed_domains = ['hot.online.sh.com']
    start_urls = ['https://hot.online.sh.cn/node/node_65634.htm']


    def parse(self, response):
        items = XinwenItem()
        datas = response.xpath('//div[@class="list_main"]/div[@class="list_thread"]')
        for data in datas:
            items['title'] = data.xpath('./h2/a/text()').extract_first()
            items['times'] = data.xpath('./h3/text()').extract_first()
            items['info'] = data.xpath('./p/text()').extract_first()
            yield items
        next_page = response.xpath('//center/a[text()="下一页"]/@href').extract_first()
        if next_page:
            base_url = 'https://hot.online.sh.cn/node/'
            url1 = urljoin(base_url,next_page)
            yield scrapy.Request(url=url1,callback=self.parse)




if __name__ == '__main__':
    cmdline.execute('scrapy crawl xinwen_spider'.split())