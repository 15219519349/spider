import json
import requests
import time
import hashlib
import execjs
import redis

class Zhihu:
    def __init__(self):
        # 地址进行了加密
        self.url = 'c0b7f0b6bb14e459bce405611045243c'
        self.redis_client = redis.StrictRedis(
            host='127.0.0.1',
            port=6379,
            db=1,
            decode_responses=True
        )

    def times(self):
        """
        负责模拟时间戳
        :return:
        """
        time_time = str(time.time()).split('.')[0]
        return time_time

    def md_5(self,text):
        """
        负责模拟md5加密
        :return:
        """
        md5 = hashlib.new('md5',text.encode('utf-8'))
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()

    def the_assembly(self):
        """
        负责加密的组装并使用md5加密
        :return:
        """
        version = '101_3_2.0'
        url = '/api/v4/articles/502532994/root_commentsorder=normal&limit=20&offset=0&status=open'
        dc0 = '"AMAQhmePsBSPThQGj3YW9GZRCnDAVC0c0XQ=|{}"'.format(self.times())
        xZst81 = "3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7eU0r6Ppb7tqXRFZQi90-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueTh8YKBvC9oqppS_NqsqtBa9LGFhVm0hgBfCYBQGeMqvNVgbLLGwL8xcLK-DCPv03CkhoByUumoLw8oJem1LLq3gHfObO8DqpGlhFLe03MrgcKqweCJgFMbhwCYJOpHwL_GCLLzhH8PcXmQDwC29VqS6eqkAOfTgoCmgNBYJwfACe1LGO0vqfz3rpOeCeXQeSq1HLqJqp0wUOVgqHOXJe1hbHLrTcM1gS9wwCYBcO9k6SL6Bg05CYBucXKyU2uihNOhUL1ObVOk9O8N9F0-9SYgGLMDUL1-cXM-wHCwrOC"
        join_ = '+'.join([version,url,dc0,xZst81])
        join_ = self.md_5(join_)
        return join_

    def js(self):
        """
        通过调用js取得加密参数
        :return:
        """
        with open('js.js', 'r', encoding='utf-8') as file:
            f = file.read()
        data = execjs.compile(f).call('b',self.the_assembly())
        return data
    def sismebmer_redis(self,key,data):
        """
        redis 判断元素是否存在
        :return:
        """

        sis = self.redis_client.sismember(key,data)
        return sis

    def run(self):
        """
        入口函数
        :return:
        """
        x_96 = '2.0_' + self.js()
        print(x_96)
        headers = {
            'accept':'*/*',
            'accept-language':'zh-CN,zh;q=0.9',
            'cache-control':'no-cache',
            'cookie':'_zap=21875815-13b2-4704-9343-7db4c00d8945; d_c0="AMAQhmePsBSPThQGj3YW9GZRCnDAVC0c0XQ=|1648226136"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=Q8e3dWmE6NhEFEFVBBN%2FrrZCSfb1s4xw; _xsrf=weVNDMkr3lsZ1Eb1sTxWuiAJ1iSa0X3E; captcha_session_v2=2|1:0|10:1650465789|18:captcha_session_v2|88:c0pId2RjT0I5bit5b2JKS3MxNUhnTUtCdTUrL2ZvNHJEaVRzNjZJaHM3dXI2YXcyam5BTGRDaTBSZUs5ZHhzZA==|3b6b7d0d422fd7a755f701baa4925056d8ae4a7a87c60246eb93e4f1965da983; __snaker__id=zjKAL1YCMynmxyxH; gdxidpyhxdE=b%5CvuyKS67yS9wmuq0HJJ35W9NO%2Fh3kPOGYTx195P2ROsaxJisDJ3M2OdpKcVt2E7s%2Fax3oioZR8WJbWSPR3GBtCcEKNvp%2FCNWukOj%2B6elBQGVK5lYOvCBDqGoxtc%2FnE1K%5Cf3lL%2BkhbOQBXuvI%2BdhvSirTlKXIsERM29we6IEGugA2KdT%3A1650466692145; YD00517437729195%3AWM_NI=3LPWBluVrQmtxN4XlQVFtVOy8pdQAREc1dSuXmJTQTclADx%2FZhFWIgK%2F%2BpGJ3cGsBG8hu7%2FABCBm%2FpSX6cOQR2I1LXIhlFnY2ZUZeqH3wX4AyVCrA4yXVdsUwb0HO2OvdUs%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee89dc61fc899cd7d86af3968fa6d45a878f8bb0c44b818afaace852abf5a899ef2af0fea7c3b92af194a0b8c168b78abeb2f080bc92fcb9ef5b969abcb7ce73fcb0acb2c45a87bdff85d27f9cb386b5d460a1b48fa5fb259ab88ab8cc6d89f1e591c642f1bd8994c14dfcb8bbd8ae4b829d8e8eae7c9188fa84ce5b92ee87d2cf548bb8a4a7ed53f2869bbbe87b8cedb9b9b74bbb8a8d93c440bb889a85f25fb5be00a9ce3a8daaacb6f237e2a3; l_cap_id="Yjg0N2RmZjNiN2IzNGI2MDgwMTU2N2VmYjMxMjBlNGY=|1650465827|19059b4546e34a00e28abfbfffc16d444a0ae234"; r_cap_id="ZDkzMjQxNjNiYWZiNGRiYTgyNjIxYmY4OGI2MjNjZGQ=|1650465827|e9c40b1fffc3bbd6091f22418ca5c1ba4eb39e74"; cap_id="YTIwODM3NzFmYzY1NGQ5ZDgyYzg0ODY5Mzg0NjVmYmY=|1650465827|542c3f7a9f75811a45f34aafba132a8a61863410"; z_c0=2|1:0|10:1650465839|4:z_c0|92:Mi4xbTdHVExBQUFBQUFBd0JDR1o0LXdGQmNBQUFCZ0FsVk5MMnBOWXdDei0tU0o3OFQzWWNZcnJHalVHelprZ1Y4c1JR|c62a38109867870b94fab7debacbd618165f1e9caa77402b0b86aa0e98fb3d93; q_c1=d2a63dfd29e44b2d8ac78a609c7698f6|1650465840000|1650465840000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1649345740,1650207960,1650465790,1650632230; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1650632230; tst=r; NOT_UNREGISTER_WAITING=1; SESSIONID=ZoygFaAwQNetoMsmpe5xfRLGrcunjd3u6d66swEuYy6; JOID=UloXBUpOqyPnqmWFdki4fqxpZDVgFsReh-0GxAUe50aXwin0G2QJQoOpZ4F1R9kmL3ZAcApB0YuyIUvm0dovWFg=; osd=W1gTAElHqSfiqWyHck27d65tYTZpFMBbhOQEwAAd7kSTxyr9GWAMQYqrY4R2TtsiKnVJcg5E0oKwJU7l2NgrXVs=; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1650632247|1650632228',
            'pragma':'no-cache',
            'referer':'https://www.zhihu.com/',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'x-ab-param':'top_test_4_liguangyi=1;tp_contents=2;se_ffzx_jushen1=0;qap_question_visitor= 0;qap_question_author=0;pf_adjust=0;pf_noti_entry_num=2;tp_dingyue_video=0;tp_topic_style=0;tp_zrec=1',
            'x-ab-pb':'CpYCwwnxCaYGyQlCCTIDPwY7AvYCNAzcC1cElAbcB/MDmwsxBmYH2gjRCYwF2AeiBjMEiwXlCfQDPwBAAasJ1wvFCPYJdAgnCcoJoQPrBikF4wUyBXsHTwdnCFUJYQnMCeAL3QfWCA8LMwU/CWALUANXBycH5QgBC2kBUgWjCdcCVAkrCsUJjQRSCxsAQwCbBwIIxgl4B40JzAIwBnUJyAkRBekEBgqMBBYG4QlWDKADFgmeBeAJogN5CHYIYAnWBLkCUQW0AGoBRwC1C5gIxAl6CMsJdweJCEkJ5Aq3A0EGhAk3DCoDpgQnCAEJBAq0CoQCzwuyB8cJ5wWRCSoG9At9AosJbAh0AdgC9AlWBRIJAQYHCuwKTwMSiwEAAAAAAAAAAAAAAAEAAgACAQEAAAAAAAAAAAAAAQEAAAAAAAAAAAAAAAAABQAAAAACAAECAAAAAQAAAAAAAAAAAAAEAQAVAAEAAAAAAQAAAAAABAAAAQAAAQAAAAABBBUBAAEAAwMAAAAAAAEAAAAAAQIAAAAAAAALAwAAAQAAAQUAAAAAAAAAAAEA',
            'x-app-version':'6.42.0',
            'x-requested-with':'fetch',
            'x-zse-93':'101_3_2.0',
            'x-zse-96':x_96,
            'x-zst-81':'3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7eU0r6Ppb7tqXRFZQi90-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueTh8YKBvC9oqppS_NqsqtBa9LGFhVm0hgBfCYBQGeMqvNVgbLLGwL8xcLK-DCPv03CkhoByUumoLw8oJem1LLq3gHfObO8DqpGlhFLe03MrgcKqweCJgFMbhwCYJOpHwL_GCLLzhH8PcXmQDwC29VqS6eqkAOfTgoCmgNBYJwfACe1LGO0vqfz3rpOeCeXQeSq1HLqJqp0wUOVgqHOXJe1hbHLrTcM1gS9wwCYBcO9k6SL6Bg05CYBucXKyU2uihNOhUL1ObVOk9O8N9F0-9SYgGLMDUL1-cXM-wHCwrOC',
            }
        res = json.loads(requests.get(url=self.url,headers=headers).text)
        datas = res.get('data')
        # key = self.redis_client.sadd()
        for data in datas:
            name = data.get('author').get('member').get('name')
            content = data.get('content')
            print(name,content)




if __name__ == '__main__':
    z = Zhihu()
    z.run()