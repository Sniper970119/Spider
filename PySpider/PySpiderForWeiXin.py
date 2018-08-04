#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-03 19:59:52
# Project: weixin

from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    crawl_config = {

    }
    cookies = 'CXID=0DDCDF3AB524336D02F12EE46CD334E4; SUID=D4C85D7C3965860A5AA39D940000145A;IPLOC=CN2102; SUV=1531959792494460;sct=5; SNUID=8E67BCEBD1D5A2CE38998221D186284B;ld=wyllllllll2bFdo5lllllVH5TZGlllllnLLdflllllwlllll9Zlll5@@@@@@@@@@; LSTMV=347%2C155; LCLKINT=4472; ABTEST=0|1531961096|v1; weixinIndexVisited=1; JSESSIONID=aaa4Ta7_4rS8e9Jqz3Hsw; ppinf=5|1532852075|1534061675|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTclOUYlQjMlRTUlQTQlQjR8Y3J0OjEwOjE1MzI4NTIwNzV8cmVmbmljazoxODolRTclOUYlQjMlRTUlQTQlQjR8dXNlcmlkOjQ0Om85dDJsdUI5VE85TE1CemdVRDd5dC10RjI4MzBAd2VpeGluLnNvaHUuY29tfA; pprdig=Lk7HiV8rT2LS8uZh0riBcnZ8cokN-aN-Yv5OjbnX3qmZS4SYIg7PnnZqXWsxfPwNF1M-YxeT9PZQxGVw7qc6d15IjwIg_2E9537JOqzdHQL34_9ntlXJ_gYE7RCQ-Nt_piMGk9cvi5Ll9oRWWsdK2dUqWTbDnESGbkA07hWhO9E; sgid=06-34211517-AVtdd2sgghdVYlHDIz6Ug1U; ppmdig=153286085500000088c26503f3219f8b3403a4a6915fc676'

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://weixin.sogou.com/weixin?type=2&query=RNG', callback=self.index_page, fetch_type='js'
                   , age=5 * 24 * 60 * 60, auto_recrawl=True)
        print('start')

    @config(age=5 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.news-box .news-list li .txt-box h3 a').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js')
        next = response.doc('.np').attr.href
        print('add next')
        self.crawl(next, callback=self.index_page, fetch_type='js', cookies=self.cookies)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            'title': response.doc('.rich_media_title').text(),
            'content': response.doc('.rich_media_content').text(),
            'date': response.doc('#publish_time').text(),
            'nickname': response.doc('#js_profile_qrcode > div > strong').text(),
            'wechat': response.doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }

    def on_result(self, result):
        if result:
            self.insert_result(result)
        super(Handler, self).on_result(result)

    def insert_result(self, result):
        print(result)
        if result:
            client = pymongo.MongoClient(host='127.0.0.1', port=27017)
            db = client['Test']
            coll = db['WeiXinPy']
            data = {
                "url": result['url'],
                'title': result['title'],
                'content': result['content'],
                'date': result['date'],
                'nickname': result['nickname'],
                'wechat': result['wechat']
            }
            print('save')
            data_id = coll.insert(data)

