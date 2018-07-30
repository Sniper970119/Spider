# -*- coding:utf-8 -*-

from aip import AipOcr
from PIL import Image
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = '18742037051'
PASSWORD = 'zhaoyu.0209'

# by baiduOCR
# APP_ID = '105649896'
# API_KEY = 'xnOIoKcX44zUxYuca6qComZQ6'
# SECRET_KEY = 'UOIp0fMt3YQSiR6jjsf875td3eZEiw306'
#
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
#
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
#
# image = get_file_content('./file/code/01.png')
#
# # """ 调用通用文字识别, 图片参数为本地图片 """
# words = client.basicGeneral(image)
# print(words)


# weibo code
# class CracjWeiboSlide():
#     def __init__(self):
#         self.url = 'https://passport.weibo.cn/signin/login'
#         self.browser = webdriver.Chrome()
#         self.wait = WebDriverWait(self.browser, 10)
#         self.username = USERNAME
#         self.password = PASSWORD
#
#     def __del__(self):
#         self.browser.close()
#
#     def open(self):
#         self.browser.get(self.url)
#         username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
#         password = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
#         submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
#         username.send_keys(self.username)
#         password.send_keys(self.password)
#         submit.click()
#
#     def get_position(self):
#         img = None
#         try:
#             img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'patt-shadow')))
#         except TimeoutException:
#             print('未出现验证码')
#             self.open()
#         time.sleep(2)
#         location = img.location
#         size = img.size
#         top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
#             'width']
#         return (top, bottom, left, right)
#
#     def get_scrennshot(self):
#         screenshot = self.browser.get_screenshot_as_png()
#         screenshot = Image.open(BytesIO(screenshot))
#         return screenshot
#
#     def get_image(self, name='captcha.png'):
#         top, bottom, left, right = self.get_position()
#         print('验证码位置', top, bottom, left, right)
#         screenshot = self.get_screenshot()
#         captcha = screenshot.crop((left, top, right, bottom))
#         captcha.save(name)
#         return captcha
#
#     def main(self):
#         count = 0
#         while True:
#             self.open()
#             time.sleep(2)
#             print(count)
#             # self.get_image(str(count) + '.png')
#             # count += 1
#
#
# if __name__ == '__main__':
#     for i in range(20):
#         crack = CracjWeiboSlide()
#         crack.main()

from urllib import request  # 要访问的目标页面

targetUrl = " http://mp.weixin.qq.com/s?src=11&timestamp=1532915404&ver=1029&signature=bxsx*WKZJn*LpSVTJ288KsMQDxXieyxGoJda1LjCl0w*zR-Rk*VDhONlm41ztogesRUul1r45flrk9UH5PQm*GwmyxJmgdvWKwYV4dFlSdYqolTSGNshgVXy9Z1J6K-8&new=1"

headers = {
    'Host': 'weixin.sogou.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'IPLOC=CN2102; SUID=5EB76D3B541C940A000000005B5D77A5; SUV=1532852134326778; ABTEST=0|1532852134|v1;'
              ' SNUID=79904A1C27225538D5D921EB27F8FEC5; weixinIndexVisited=1; sct=1; JSESSIONID=aaadRdXPO6lDNfv3W2Hsw'
}

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H44849JU5O0CUXJD"
proxyPass = "9D6530023F397B62"

import requests

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

resp = requests.get(targetUrl, proxies=proxies)

print(resp.status_code)

print(resp.text)
