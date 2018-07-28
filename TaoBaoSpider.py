# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import pymongo
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)
KEY_WORD = 'iPhone'
base_url = 'https://s.taobao.com/search?q='


def get_page(page):
    try:
        print('******获取页面源码******')
        url = base_url + KEY_WORD
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        print('******获取源码成功******')
        # time.sleep(5)
        print(browser.current_url)
        parse_page()
    except TimeoutException:
        print('Error:********获取源码超时********')


def parse_page():
    print('******截取商品信息******')
    html_code = browser.page_source
    doc = pq(html_code)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'good id': item.find('.pic .pic-link').attr('data-nid'),
            'image': item.find('.pic .img').attr('data-src'),
            'price': re.sub('\s+', '', item.find('.g_price-highlight').text()),
            'deal': item.find('.deal-cnt').text(),
            'shop': item.find('.ww-light.ww-small').attr('data-nick'),
            'shop id': item.find('.shopname').attr('data-userid'),
            'location': item.find('.location').text(),

        }
        save_to_mongo(product)


def save_to_mongo(product):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.Test
    collection = db.TaoBao
    id = product['good id']
    result = collection.find_one({'good id': id})
    if result is None:
        collection.insert(product)
        print('******保存到数据库' + str(id) + '******')
    else:
        print(str(result) + "      " + str(id))


if __name__ == '__main__':
    for page in range(1, 100):
        print('\n*******第' + str(page) + '次爬取*******')
        html = get_page(page)
        # products = parse_page(html)
        # for product in products:
        #     save_to_mongo(product)
