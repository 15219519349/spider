import execjs
import requests
import re

class Fhouse:
    def __init__(self):
        # 地址均已进行加密
        self.index_url = 'b54cea8e2e4b56ee595250356ca6f36d'
        self.login_url = '78e8850906503b44fb530a826a75a78e'
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '316',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'city=gz; global_cookie=ppil9jp5lowwexfuha9vzdnsk17l24jvvwp; token=e7ee056cde4a4bdda9963073a2787e4c; __jsluid_s=cc5bca78cccfaed7e248ac12e4e9b14a; g_sourcepage=txz_dl%5Egg_pc; unique_cookie=U_ppil9jp5lowwexfuha9vzdnsk17l24jvvwp*2; __utma=147393320.1050717383.1650276302.1650276302.1650276302.1; __utmc=147393320; __utmz=147393320.1650276302.1.1.utmcsr=gz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmb=147393320.2.10.1650276302',
            'Host': 'passport.fang.com',
            'Origin': 'https://passport.fang.com',
            'Pragma': 'no-cache',
            'Referer': 'https://passport.fang.com/?backurl=https%3A%2F%2Fgz.fang.com%2F',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        }

    def get_key(self):
        """
        负责获取key_to_encode
        :return:
        """
        session = requests.get(url=self.index_url)
        response = session.text
        key_to_encode = re.findall(r'RSAKeyPair\((.*)\);', response)[0].replace('"', '').split(', ')
        return key_to_encode

    def js_house(self):
        """
        负责js调用解密
        :return:
        """
        n, i, t = self.get_key()
        with open('js.js', 'r', encoding='utf-8') as file:
            f = file.read()
        pwd = execjs.compile(f).call("xl",password,n,i,t)
        return pwd

    def login(self):
        """
        负责整体业务逻辑
        :return:
        """
        data = {
        'uid':user,
        'pwd':self.js_house(),
        'Service':'soufun-passport-web',
        'AutoLogin':'1'
        }
        req = requests.post(url=self.login_url,headers=self.headers,data=data)
        res = req.json()
        print(res)

if __name__ == '__main__':
    house = Fhouse()
    user = input('请输入账号:').strip()
    password = input('请输入密码:').strip()
    house.login()