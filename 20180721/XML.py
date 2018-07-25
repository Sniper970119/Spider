# -*- coding:utf-8 -*-
from lxml import etree


# xml test -> tostring
# html = etree.parse('test.xml', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))


# xml test -> all
# html = etree.parse('test.xml', etree.HTMLParser())
# result = html.xpath('//*')
# print(result)


# xml test -> son
# html = etree.parse('test.xml', etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)


# xml test -> father
# html = etree.parse('test.xml', etree.HTMLParser())
# result = html.xpath('//a[@herf="link4.html"]/../@class')
# print(result)


# xml test -> get attribute
html = etree.parse('test.xml', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)


# xml test -> get attribute
html = etree.parse('test.xml', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)