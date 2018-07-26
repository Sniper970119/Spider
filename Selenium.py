# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 声明浏览器对象
# browser = webdriver.Chrome()
#
# # 访问页面
# browser.get('https://www.taobao.com')
# print(browser.page_source)
#
# # 查找单个节点
# # 使用 find_element_by_name
# input_first = browser.find_element_by_name('q')
# # 使用 XPath
# # input_second = browser.find_element_by_xpath('//*[@id="q"]')
# # 使用 CSS选择器
# # input_third = browser.find_element_by_css_selector('#q')
# input_first.send_keys('iPad')
# time.sleep(1)
# input_first.clear()
# input_first.send_keys('iPhone')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
#
# # 显示等待
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))


# 选项卡管理
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')


