import time

import pyppeteer
import asyncio
import random
from urllib import request
import cv2

params = {
    '--window-size=1920,1080'
}
async def get_img():
    bg = cv2.imread('image_bg.jpg',0)
    qk = cv2.imread('image_qk.jpg',0)
    # 归一化处理
    res = cv2.matchTemplate(bg,qk,cv2.TM_CCORR_NORMED)
    # 获取最小最大索引
    value = cv2.minMaxLoc(res)[2][0]
    value1 = value * 278/ 360
    return value1

async def main():
    browser = await pyppeteer.launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height':768 })
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                     '{ webdriver:{ get: () => false } })}')
    # 地址进行了加密
    await page.goto('2e2b96b5d18f740b08eb971da75e5ee7')
    await page.waitFor(2000)
    await page.click('div.login-tab-r')
    # await page.waitFor(2000)
    await page.type('input#loginname','15219519349',delay=random.randint(5,10))
    await page.waitFor(2000)
    await page.type('input#nloginpwd','123456',delay=random.randint(5,10))
    await page.waitFor(2000)
    await page.click('div.login-btn a')
    await page.waitFor(2000)
    # time.sleep(20)
    image_bg = await page.querySelectorEval('div.JDJRV-bigimg >img','el => el.src')
    image_qk = await page.querySelectorEval('div.JDJRV-smallimg img','el => el.src')
    request.urlretrieve(image_bg,'image_bg.jpg')
    request.urlretrieve(image_qk,'image_qk.jpg')
    distance = await get_img()
    huakuai = await page.querySelector('div.JDJRV-slide-btn')
    box = await huakuai.boundingBox()
    await page.hover('div.JDJRV-slide-btn') # 鼠标停在上面
    await page.mouse.down() # 点击鼠标
    await page.mouse.move(box['x'] + distance + random.uniform(30,33),box['y'],{'steps':30})
    await page.waitFor(random.randint(300,800))
    await page.mouse.move(box['x'] + distance +29,box['y'],{'steps':30})
    await page.mouse.up()
    time.sleep(20)
asyncio.get_event_loop().run_until_complete(main())