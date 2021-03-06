# -*- coding:utf-8 -*-
import json
import requests
import re
from requests.exceptions import RequestException


# get page code
def get_one_page(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339'
                      '6.99 Safari/537.36'
    }
    try:
        responce = requests.get(url=url, headers=headers, timeout=5)
        if responce.status_code == 200:
            return responce.text
        else:
            return None
    except RequestException:
        return None


# parse the message with regex
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?data-src="(.*?)".*?class="star">'
                         '(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>', re.S)
    items = re.findall(pattern=pattern, string=html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1].strip(),
            'image': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5].strip() + item[6].strip()
        }
    return items


# write to file
def write_to_file(content):
    with open('MaoYanSpider.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# get picture
def get_picture(content):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.339'
                      '6.99 Safari/537.36'
    }
    url = content['image']
    url = re.sub('(@.*)', "", url)
    title = content['title']
    responce = requests.get(url=url, headers=headers, timeout=5)
    with open("./image/" + title + ".jpg", 'wb') as f:
        f.write(responce.content)


# main
if __name__ == '__main__':
    offset = 0
    for i in range(10):
        url = 'http://www.maoyan.com/board/4?offset=' + str(offset)
        html = get_one_page(url)
        # f = open('maoyan.txt', 'w')  # print page code in file
        # f.write(html)
        # print(html)                  # print page code in console
        for item in parse_one_page(html):  # print the handled message
            # print(item)
            # write_to_file(item)
            get_picture(item)
        offset = offset + 10
