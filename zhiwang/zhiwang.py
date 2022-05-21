import requests
from PIL import Image
import ddddocr
import time




def request(url,headers):
    # 负责请求功能
    res = requests.get(url,headers=headers)
    return res

def yzm():
    # 识别验证码功能
    times = time.time() * 1000
    times = str(times).split('.')[0]
    # 地址进行了加密
    yzm_url = 'f65a86f01769f5dd6e91fd0a260ac1d5'.format(times)
    yzm_header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'_pk_ref=%5B%22%22%2C%22%22%2C1650979075%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DZ0NTsGbIdkS51F4H-U58tsNPJpxMXbf3eHlWfxs-6gK%26wd%3D%26eqid%3De4515adf0000f432000000066267f0fd%22%5D; _pk_id=b97c5af0-8181-4a39-ae6d-019e471550ce.1650979075.1.1650979075.1650979075.; _pk_ses=*; Ecp_ClientId=d220426211701650218; Ecp_IpLoginFail=220426117.136.12.232; ASP.NET_SessionId=szrk2co21m3puvkaxdkkw25s; SID_mycnki=020102',
        'Host':'my.cnki.net',
        'Pragma':'no-cache',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'none',
        'Sec-Fetch-User':'?1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }
    res = request(yzm_url,headers=yzm_header).content
    with open('yzm.jpg','wb') as file:
        file.write(res)
    ocr = ddddocr.DdddOcr(old=True)
    with open("yzm.jpg", 'rb') as f:
        image = f.read()

    res = ocr.classification(image)
    return res

def register():
    # 注册账号功能
    yzm_result = yzm() # 验证码结果
    # 地址进行了加密
    url = '913a73047d4c0b4390e845f3977bd24b'.format(yzm_result.upper())
    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Host':'my.cnki.net',
        'Referer':'https://my.cnki.net/Register/CommonRegister.aspx?returnurl=http%3a%2f%2fwww.cnki.net%2f',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    cookie = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'_pk_ref=%5B%22%22%2C%22%22%2C1650979075%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DZ0NTsGbIdkS51F4H-U58tsNPJpxMXbf3eHlWfxs-6gK%26wd%3D%26eqid%3De4515adf0000f432000000066267f0fd%22%5D; _pk_id=b97c5af0-8181-4a39-ae6d-019e471550ce.1650979075.1.1650979075.1650979075.; _pk_ses=*; Ecp_ClientId=d220426211701650218; Ecp_IpLoginFail=220426117.136.12.232; ASP.NET_SessionId=szrk2co21m3puvkaxdkkw25s; SID_mycnki=020102',
    'Host':'my.cnki.net',
    'Pragma':'no-cache',
    'Referer':'https://my.cnki.net/Register/CommonRegister.aspx?returnurl=http%3a%2f%2fwww.cnki.net%2f',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    res = requests.get(url=url,headers=headers,cookies=cookie)
    print(res.text)

if __name__ == '__main__':
    register()