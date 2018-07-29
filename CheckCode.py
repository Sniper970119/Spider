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
class CracjWeiboSlide():
    def __init__(self):
        self.url = 'https://passport.weibo.cn/signin/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)
        self.username = USERNAME
        self.password = PASSWORD

    def __del__(self):
        self.browser.close()

    def open(self):
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

    def get_position(self):
        img = None
        try:
            img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'patt-shadow')))
        except TimeoutException:
            print('未出现验证码')
            self.open()
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_scrennshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_image(self, name='captcha.png'):
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def main(self):
        count = 0
        while True:
            self.open()
            time.sleep(2)
            print(count)
            # self.get_image(str(count) + '.png')
            # count += 1


if __name__ == '__main__':
    for i in range(20):
        crack = CracjWeiboSlide()
        crack.main()
