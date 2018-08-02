# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = TutorialItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        # 获取下一页链接
        next = response.css('.pager .next a::attr("href")').extract_first()
        # 处理绝对链接
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
