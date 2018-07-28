# -*- coding:utf-8 -*-

from aip import AipOcr
from PIL import Image

APP_ID = '105649896'
API_KEY = 'xnOIoKcX44zUxYuca6qComZQ6'
SECRET_KEY = 'UOIp0fMt3YQSiR6jjsf875td3eZEiw306'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('./file/code/01.png')

# """ 调用通用文字识别, 图片参数为本地图片 """
words = client.basicGeneral(image)
print(words)

