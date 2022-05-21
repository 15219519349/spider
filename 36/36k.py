import execjs
import requests
import time
class Kr36:
    def __init__(self):
        # 地址进行了加密
        self.login_url = '0cacf1d99efdc97a4383ca4dc60f979f'
        self.headers = {
            'accept':'*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'cache-control':'no-cache',
            'content-length':'460',
            'content-type':'application/json',
            'cookie':'Hm_lvt_713123c60a0e86982326bae1a51083e1=1649162076,1650263245; Hm_lvt_1684191ccae0314c6254306a8333d090=1649162076,1650263245; acw_tc=2760776e16502632467838568e939027b725de819644e4792b72d27c5f5e7f; userId=5738206; krnewsfrontcc=eyJ0eXAiOiJKV1QiLCJhbGciOiIzNmtyLWp3dCJ9.eyJpZCI6NTczODIwNiwic2Vzc2lvbl9pZCI6Ijg2ZDA2NzQwZmYyYWUxN2YxOTBlZmU2YjRhYmU0MDdlIiwiZXhwaXJlX3RpbWUiOjE2NTAwMDcyMTQsInZlcnNpb24iOiJ2MSJ9.b293488f1bb6bb8493f47224116d5374def1ba8f63b44c41a5c64fc6f182bbf6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225738206%22%2C%22%24device_id%22%3A%2217ff9b83dd313c-09bd15d2fdd41c-9771a39-1327104-17ff9b83dd4d60%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2217ff9b83dd313c-09bd15d2fdd41c-9771a39-1327104-17ff9b83dd4d60%22%7D; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1650264044; Hm_lpvt_1684191ccae0314c6254306a8333d090=1650264044',
            'origin':'https://36kr.com',
            'pragma':'no-cache',
            'referer':'https://36kr.com/',
            'sec-ch-ua':'"Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-site',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        }

    def js(self,text):
        """
        负责调用js解密
        :param text:
        :return:
        """
        with open('JS.js','r',encoding='utf-8') as f:
            js = f.read()
        js1 = execjs.compile(js)
        text = js1.call("xl",text)
        return text

    def times(self):
        """
        负责模拟时间戳
        :return:
        """
        timestamp = str(time.time() * 1000).split('.')[0]
        return timestamp

    def run(self):
        """
        整体业务逻辑
        :return:
        """
        data = {
            'param':{
                'countryCode':'86',
                'mobileNo':'{}'.format(self.js('15219519349')),
                'password':'{}'.format(self.js('123456ab')),
            },
            'partner_id':'web',
            'timestamp':'{}'.format(self.times()),
        }
        res = requests.post(url=self.login_url, headers=self.headers, json=data)
        print(res.text)
if __name__ == '__main__':
    ke36 = Kr36()
    ke36.run()
