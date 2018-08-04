#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-03 19:59:52
# Project: weixin

from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    key_word = 'RNG'

    crawl_config = {

    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://weixin.sogou.com/weixin?type=2&query=' + self.key_word, callback=self.index_page,
                   fetch_type='js'
                   , age=5 * 24 * 60 * 60, auto_recrawl=True)
        print('start')

    @config(age=5 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.news-box .news-list li .txt-box h3 a').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js')
        next = response.doc('.np').attr.href
        print('add next')
        self.crawl(next, callback=self.index_page, fetch_type='js')

    @config(priority=2)
    def detail_page(self, response):
        return {
            'url': response.url,
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
                'key_word': self.key_word,
                'url': result['url'],
                'title': result['title'],
                'content': result['content'],
                'date': result['date'],
                'nickname': result['nickname'],
                'wechat': result['wechat']
            }
            print('save')
            data_id = coll.insert(data)

