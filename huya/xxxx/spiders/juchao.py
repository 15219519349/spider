import scrapy
from scrapy import cmdline
from scrapy.utils import log

page = 1
class JuchaoSpider(scrapy.Spider):
    name = 'juchao'
    allowed_domains = ['cninfo.com']
    # start_urls = ['http://cninfo.com/']
    def start_requests(self):
        start_urls = 'http://www.cninfo.com.cn/new/disclosure'
        data = {
            'column':'szse_gem_latest',
            'pageNum':str(page),
            'pageSize':'30',
            'clusterFlag':'true',
        }
        yield scrapy.FormRequest(url=start_urls,formdata=data,meta={'page':data.get('pageNum')})
    def parse(self, response):
        log.logger.warning('正在采集第{}页的数据'.format(response.meta.get('page')))
        totalpages = response.json().get('totalpages')
        datas = response.json().get('classifiedAnnouncements')
        for data in datas:
            print(data[0].get('announcementTitle'))
        global page
        page += 1
        if page <= totalpages:
            start_urls = 'http://www.cninfo.com.cn/new/disclosure'
            data = {
                'column': 'szse_gem_latest',
                'pageNum': str(page),
                'pageSize': '30',
                'clusterFlag': 'true',
            }
            yield scrapy.FormRequest(url=start_urls, formdata=data, meta={'page': data.get('pageNum')},dont_filter=True)


if __name__ == '__main__':
    cmdline.execute('scrapy crawl juchao'.split())