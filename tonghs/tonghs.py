import requests
import execjs
import hashlib
import time

class Tonghuashun:
    def __init__(self):
        # 地址进行了加密
        self.login_url = '557e01cfbbae21bcf9ef27de2493106c'
        self.headers = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Content-Length':'664',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'hexin-v':'AyImEY5htCLx_6jBjJN6wW5uc6OBcyII2HoasWyHTyZB78wdVAN2nagHaso_',
            'Host':'upass.10jqka.com.cn',
            'Origin':'https://upass.10jqka.com.cn',
            'Pragma':'no-cache',
            'Referer':'https://upass.10jqka.com.cn/login?redir=HTTP_REFERER',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        }
    def md_5(self,pwd):
        """
        密码md5逻辑
        :return:
        """
        md5 = hashlib.new('md5',pwd.encode('utf-8'))
        md5 = hashlib.md5()
        md5.update(pwd.encode('utf-8'))
        return md5.hexdigest()

    def js(self,text):
        """
        读取js中的加密逻辑
        :return:
        """
        with open('js.js', 'r', encoding='utf-8') as file:
            f = file.read()
        js = execjs.compile(f).call('encryptEncode',text)
        return js

    def times(self):
        timestamp = str(time.time()).split('.')[0]
        return timestamp

    def login(self):
        cookie = {
            "Cookie": "log=;Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1650462766; PHPSESSID=4p089m0k307ibs9kpfq5ragg4lfb0egs; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1650462898;v=AyImEY5htCLx_6jBjJN6wW5uc6OBcyII2HoasWyHTyZB78wdVAN2nagHaso_"
        }
        data = {
        'uname':self.js(user),
        'passwd':self.js(self.md_5(password)),
        'longLogin':'0',
        'rsa_version':'default_4',
        'source':'pc_web',
        'request_type':'login',
        'captcha_type':'4',
        'captcha_phrase':'158;38.17058823529412;309;177.22058823529412',
        'captcha_ticket':'bf12bbce14081862b79c19aebdb2c021',
        'captcha_signature':'218043e78eaf62c31938df4e0f4c5d70',
        'ttype':'WEB',
        'sdtis':'C22',
        'timestamp':self.times()
        }
        print(data)
        # res = requests.post(url=self.login_url,headers=self.headers,data=data)
        # print(res.text)

    def run(self):
        """
        入口函数
        :return:
        """
        self.login()

if __name__ == '__main__':
    user = input('请输入账号:').strip()
    password = input('请输入密码:').strip()
    t = Tonghuashun()
    t.times()