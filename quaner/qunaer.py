from selenium import webdriver
import time
from lxml import etree
import re
# 地址进行了加密
url = '5edfb1c0596fc8d3d0b926a13e53dd7a'
def qunaer():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)
    browser.implicitly_wait(5)
    div = browser.find_element_by_xpath('//div[@class="btn-box"]/div')
    div.click()
    time.sleep(5)
    divs = browser.find_elements_by_xpath('//div[@class="mb-10"]/div/div')
    for div in divs:
        name = div.find_element_by_xpath('.//div[@class="air"]').text
        start_time = div.find_element_by_xpath('.//div[@class="sep-lf"]/h2').text
        end_time = div.find_element_by_xpath('.//div[@class="sep-rt"]/h2').text
        prices = div.find_elements_by_xpath('.//div[@class="col-price"]//em[@class="rel"]/b/i')
        price = [price.text for price in prices]
        to_cover_prices = div.find_elements_by_xpath('.//div[@class="col-price"]//em[@class="rel"]/b')
        to_cover_prices_and_styles = [
            (to_cover_price.text, to_cover_price.get_attribute('style')) for to_cover_price in to_cover_prices[1:]
        ]
        # print(to_cover_prices_and_styles)
        for to_cover_price, to_cover_style in to_cover_prices_and_styles:
            left = re.search('width: 16px; left: -(\d+)px;', to_cover_style).group(1)
            price[-int(left) // 16] = to_cover_price
        price = ''.join(price)
        print(name,start_time,end_time,price)
qunaer()