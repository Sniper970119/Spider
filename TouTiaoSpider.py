# -*- coding:utf-8 -*-
from urllib.parse import urlencode
import requests
import pymongo


base_url = 'https://www.toutiao.com/api/pc/feed/?'
headers = {
    'referer': 'https://www.toutiao.com/ch/news_tech/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/67.0.3396.99 Safari/537.36',
    'cookie': 'tt_webid=6582430453025900040; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=164d592b6b577c-'
              '01bbb425c262e8-47e1039-1fa400-164d592b6b6193; CNZZDATA1259612802=1935731616-1532588410-'
              'https%253A%252F%252Fwww.baidu.com%252F%7C1532588410; tt_webid=6582430453025900040; __'
              'tasessionId=fm5a1x2sm1532591519911; csrftoken=4298418f9ec85b57aa4d9e5b781bed87;'
              ' uuid="w:a033d21de37d453780932620f5d81416"',
    'x-requested-with': 'XMLHttpRequest'
}

attrs = {
    'category': 'news_tech',
    'utm_source': 'toutiao',
    'widen': '1',
    'max_behot_time': '0',
    'max_behot_time_tmp': '0',
    'tadrequire': 'true',
    'as': 'A1353B4569B7E17',
    'cp': '5B59A71E724A1E1',
    '_signature': 'g9UFGQAA2Jkp-kWZLlPu9YPVBQ'
}


# get page
def get_page():
    url = base_url + urlencode(attrs)
    try:
        responce = requests.get(url=url, headers=headers)
        if responce.status_code == 200:
            return responce.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


# parse the json
def parse_page(json):
    if json:
        items = json.get('data')
        for item in items:
            toutiao = {}
            toutiao['id'] = item['group_id']
            toutiao['title'] = item['title']
            if 'chinese_tag' in item:
                toutiao['chinese_tag'] = item['chinese_tag']
            else:
                toutiao['chinese_tag'] = 'NULL'
            if 'comments_count' in item:
                toutiao['comments_count'] = item['comments_count']
            else:
                toutiao['comments_count'] = 'NULL'
            if 'image_url' in item:
                toutiao['image_url'] = item['image_url']
            else:
                toutiao['image_url'] = 'NULL'
            toutiao['is_feed_ad'] = item['is_feed_ad']
            toutiao['source'] = item['source']
            toutiao['source_url'] = item['source_url']
            yield toutiao


# save in mongo
def save_to_mongo(result):
    id = result['id']
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.Test
    collection = db.TouTiao
    if_have = collection.find_one({'id': id})
    if if_have is None:
        collection.insert(result)


# main
if __name__ == '__main__':
    for i in range(100):
        json = get_page()
        results = parse_page(json)
        for result in results:
            save_to_mongo(result)

