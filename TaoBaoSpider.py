# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from urllib.parse import quote

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 10)
KEY_WORD = 'iPhone'
base_url = 'https://s.taobao.com/search?q='


def get_page(page):
    url = base_url + KEY_WORD
    browser.get(url)
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit ')))
    input.clear()
    input.send_keys(page)
    submit.click()
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.m-itemlist .items .item.J_MouserOnverReq')))
    return browser.page_source


def parse_page(html_code):
    doc = pq(html_code)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        # print(item)
        product = {
            'title': item.find('.pic img').attr('alt'),      # wrong
            # 'image': item.find('.pic .img').attr('data-src')  # ok
            'id': item.find('.pic .pic-link').attr('data-nid')
            # 'title': item.find('.pic .J_ItemPic.img').attr('alt')  # ok

        }
        yield product


if __name__ == '__main__':
    html = get_page(0)
    products = parse_page(html)
    for product in products:
        print(product)
