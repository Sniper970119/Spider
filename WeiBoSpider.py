# -*- coding:utf-8 -*-
from urllib.parse import urlencode
import pymongo
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2656260571',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '67.0.3396.99 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


# get page code
def get_page(page):
    params = {
        'type': 'uid',
        'value': '2656260571',
        'containerid': '1076032656260571',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


# parse the code
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item['id']
            weibo['text'] = item['text']
            weibo['attitudes'] = item['attitudes_count']
            weibo['comment'] = item['comments_count']
            weibo['reposts'] = item['reposts_count']
            yield weibo


# save to database
def save_to_mongo(result):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.WeiBoTest
    collection = db.WeiBo
    collection.insert(result)


# main
if __name__ == '__main__':
    for page in range(1, 15):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            print()
            save_to_mongo(result)
