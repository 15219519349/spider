import requests
import execjs

for i in range(1,21):
    # 地址进行了加密
    url = '742c2858767c80007a97011cba5c913b'.format(i)
    headers = {
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'cache-control':'no-cache',
        'origin':'https://static.waitwaitpay.com',
        'pragma':'no-cache',
        'referer':'https://static.waitwaitpay.com/',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-site',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro me/101.0.4951.54 Safari/537.36',
    }

    res = requests.get(url=url,headers=headers)
    with open('js1.js', encoding='utf-8') as f:
        file = f.read()
    js = execjs.compile(file).call('xl',res.text)
    list1 = js.get('result').get('list')
    for data in list1:
        name = data.get('name')
        print("商家名称:",name)
        datas = data.get('recommand_vouchers')
        avg_price = data.get('avg_price')
        print('商家均价:',avg_price)
        stars = data.get('stars')
        print('商家星级:',stars)
        for z in datas:
            youhuijuan = z.get('title')
            print('商家优惠券:',youhuijuan)