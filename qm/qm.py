import execjs
import requests
params = {
    'brand':'all',
    'genre':'36',
    'device':'ipad',
    'country':'cn'
}
path = '/rank/indexPlus/brand_id/1'
with open('js.js', 'r', encoding='utf-8') as file:
    f = file.read()
js = execjs.compile(f).call("qimai",params)
headers = {
    "authority": "api.qimai.cn",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "cache-control": "no-cache",
    "origin": "https://www.qimai.cn",
    "pragma": "no-cache",
    "referer": "https://www.qimai.cn/",
    "sec-ch-ua": "^\\^",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}
# 地址进行了加密
url = 'a66cdef7f8c1cfaad4b400e42707c76d'.format(js)
res = requests.get(url=url,headers=headers,params=params)
print(res.json())