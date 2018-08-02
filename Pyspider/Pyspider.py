#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-08-02 16:50:26
# Project: qunar

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://travel.qunar.com/travelbook/list.htm', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('li > .tit > a').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js')
        next = response.doc('.next').attr.href
        self.crawl(next, callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            'date': response.doc('.when .data').text(),
            'day': response.doc('.howlong .data').text(),
            'who': response.doc('.who .data').text(),
            'text': response.doc('#b_panel_schedule').text(),
            'image': response.doc('.cover_img').attr.src
        }
