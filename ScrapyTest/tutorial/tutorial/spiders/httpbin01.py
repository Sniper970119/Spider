# -*- coding: utf-8 -*-
import scrapy
from conda.gateways import logging


class Httpbin01Spider(scrapy.Spider):
    name = 'httpbin01'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.text)


