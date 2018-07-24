# -*- coding:utf-8 -*-
import requests


def get_one_page(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    responce = requests.get(url=url, headers=headers, timeout=5)
    if responce.status_code == 200:
        return responce.text
    else:
        return None


if __name__ == '__main__':
    url = 'http://www.maoyan.com/board/4'
    html = get_one_page(url)
    f = open('maoyan.txt', 'w')
    f.write(html)
    print(html)
