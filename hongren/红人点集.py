import json
import requests
from hashlib import md5
import time
import hashlib
from loguru import logger
import pymongo

class Red_point:

    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1',27017)
        self.collection = self.client['红人点集']['data']
        # 地址均已进行加密
        self.login_url = '5787b9b28dc85ceacd8ba200a837956a'
        self.content_url = 'c09dbac3a25a48d958609829acec308f'
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '137',
            'Content-Type': 'application/json',
            'Host': 'user.hrdjyun.com',
            'Origin': 'http://www.hh1024.com',
            'Pragma': 'no-cache',
            'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        }
    def md5(self,text):
        """
        md5加密算法
        :param text:
        :return:
        """
        md = md5()
        md.update(text.encode('utf-8'))
        result = md.hexdigest()
        return result

    def request(self,url,data):
        response = requests.post(url=url,headers=self.headers,data=data)
        return response

    def times(self):
        """
        模拟时间戳
        :return:
        """
        timestamp = time.time() * 1000
        timestamp = str(timestamp).split('.')[0]
        return timestamp

    def login(self):
        """
        登录方法
        :return:
        """
        phoneNum = '15219519349'
        pwd = self.md5('123456ab')
        tenant = '1'
        sig = self.md5(phoneNum + pwd + str(self.times()) + tenant + "JzyqgcoojMiQNuQoTlbR5EBT8TsqzJ")
        data = {
          'phoneNum':phoneNum,
          'pwd':pwd,
          'sig':sig, 
          't':self.times(),
          'tenant':tenant
        }
        response = self.request(self.login_url,json.dumps(data))
        token = response.json()
        with open('token.txt','wt',encoding='utf-8') as file:
            file.write(token.get('data').get('token'))

    def sha256(self,text):
        sha = hashlib.new('sha256',text.encode('utf-8'))
        result = sha.hexdigest()
        return result

    def data(self):
        """
        获取数据data
        :return:
        """
        with open('token.txt','rt',encoding='utf-8') as f:
            token = f.read()
        year = input('请输入要查看的年份(例如2022):').strip()
        month = input('请输入要查看的月份(例如04,05):').strip()
        day = input('请输入要查看的哪一天(例如01,02):').strip()
        param = '{"no":"dy0002","data":{"days":1,"rankType":5,"liveDay":"%s-%s-%s"}}' % (year, month, day)  # 主播带货销量榜
        param1 = '{"no":"dy0002","data":{"days":1,"rankType":6,"liveDay":"%s-%s-%s"}}' % (year, month, day)  # 销售额榜
        salt = 'kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$'  # 加盐参数
        sign = f'param={param}&timestamp={self.times()}&tenant=1&salt={salt}'
        sign = self.sha256(sign)
        sign1 = f'param={param1}&timestamp={self.times()}&tenant=1&salt={salt}'
        sign1 = self.sha256(sign1)
        data = {
            'param':param,
            'tenant':'1',
            'timestamp':self.times(),
            'token':token,
            'sign':sign
        }
        data1 = {
            'param':param1,
            'tenant':'1',
            'timestamp':self.times(),
            'token':token,
            'sign':sign1
        }
        return data,data1

    def parse(self,res):
        data_list = []
        for i in res:
            anchorName = i.get('anchorName')  # 主播名称
            fans = i.get('fans')  # 主播粉丝数
            salesVolume = i.get('salesVolume')  # 主播带货销量
            salesMoney = i.get('salesMoney')  # 主播带货销售额
            data_content = {
                '主播名称': anchorName,
                '主播粉丝数': fans,
                '主播带货销量': salesVolume,
                '主播带货销售额': salesMoney
            }
            data_list.append(data_content)
        return data_list

    def save_mongo(self,data):
        """
        数据入库逻辑
        :return:
        """
        if isinstance(data,dict):
            self.collection.insert_one(data)
        else:
            logger.debug('数据格式不对')

    def get_data(self):
        """
        获取榜单数据
        :return:
        """
        bangdan = input('请输入要查看的榜单(主播带货销量榜/主播带货销售额榜)').strip()
        try:
            if bangdan == '主播带货销量榜':
                data = self.data()
                res = self.request(self.content_url,data=json.dumps(data[0])).json().get('data').get('rankList')
                data_list = self.parse(res)
                for i in data_list:
                    # self.save_mongo(i)
                    logger.info(i)
            elif bangdan == '主播带货销售额榜':
                data1 = self.data()
                res1 = requests.post(url=self.content_url,headers=self.headers,json=data1[1]).json().get('data').get('rankList')
                data_list1 = self.parse(res1)
                for o in data_list1:
                    logger.info(o)
                    # self.save_mongo(o)
            else:
                logger.debug('其他榜单正在努力开发中!!')
        except Exception as e:
            logger.debug('请输入正确的年份、月份以及哪一天!!')
            logger.debug('本接口只能提供两天内的数据！！')

    def run(self):
        """
        整体业务逻辑
        :return:
        """
        # self.login()  无token再进行开启
        self.get_data()



if __name__ == '__main__':

    a = Red_point()
    a.run()