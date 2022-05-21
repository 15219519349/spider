import requests
import re

class Mazhang:
    def __init__(self):
        # 地址进行了加密
        self.index_url = '18c3827f09ad5b067175f285e65e3011'
        self.index_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }
        self.data_url = '95125bb2a802f44fc291528c5983854a'

    def get_cookie(self):
        """
        获取cookie反爬虫的参数
        :return:
        """
        res1 = requests.get(url=self.index_url,headers=self.index_headers)
        szxx_session = res1.cookies.get('szxx_session')
        token = re.findall("var _CSRF = '(.*?)';",res1.text)[0]
        return szxx_session,token

    def request_data(self):
        session, token = self.get_cookie()
        """
        请求数据
        :return:
        """
        data = {
            'offset':'0',
            'limit':'20',
            'site_id':'759010'
        }
        cookie = {
            'Cookie': 'td_cookie=2545817991',
            'szxx_session': session,
            'XSRF-TOKEN': token
        }
        data_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'X-CSRF-TOKEN': token
        }
        res = requests.post(url=self.data_url,headers=data_headers,cookies=cookie,data=data)
        print(res.text)

    def run(self):
        """
        总体业务逻辑
        :return:
        """
        self.request_data()

if __name__ == '__main__':
    m = Mazhang()
    m.run()