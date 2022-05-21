import requests
import execjs
import json
import pymysql

client = pymysql.connect(user='root',password='',host='127.0.0.1',port=3306,db='jianzhu',charset='utf8')
cursor = client.cursor()
sql = 'insert into jz (name,company_name,login_address) values (%s,%s,%s)'
headers = {
'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1650119717,1650198586,1652197472; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1652197472',
'Host':'jzsc.mohurd.gov.cn',
'Pragma':'no-cache',
'Referer':'http://jzsc.mohurd.gov.cn/data/company',
'timeout':'30000',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
}
for i in range(30):
    # 地址进行了加密
    url = 'aa9c5a3b654c590d5415256a541f6b1a'
    params = {
    'pg':i,
    'pgsz':'15',
    'total':'450'
    }
    res = requests.get(url=url,headers=headers,params=params)
    with open('js.js',encoding='utf-8') as file:
        f = file.read()
    js = json.loads(execjs.compile(f).call('getDecryptedData',res.text))
    list1 = js.get('data').get('list')
    for data in list1:
        name = data.get('QY_FR_NAME')
        company_name = data.get('QY_NAME')
        login_address = data.get('QY_REGION_NAME')
        cursor.execute(sql,(name,company_name,login_address))
        client.commit()
cursor.close()
client.close()


