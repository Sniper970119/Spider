# -*- coding:utf-8 -*-
from lxml import etree
from bs4 import BeautifulSoup
import re
from pyquery import PyQuery as pq

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
# html = etree.parse('test.xml', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)


# xml test -> get attribute which have more than one values
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)


# xml test -> match message by more than one attribute
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")and @name="item"]/a/text()')
# print(result)


# xml test -> output by order
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')         # print the first node
# print(result)
# result = html.xpath('//li[last()]/a/text()')    # print the last node
# print(result)
# result = html.xpath('//li[position<3]/a/text()')    # print the nodes whose position is smaller than 3
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')  # print the antepenultimate node
# print(result)


# xml test -> node axle
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/ancestor::*')
# print(result)
# result = html.xpath('//li[1]/ancestor::div')
# print(result)
# result = html.xpath('//li[1]/attribute::*')
# print(result)
# result = html.xpath('//li[1]/child::a[@href="link1.html"]')
# print(result)
# result = html.xpath('//li[1]/descendant::span')
# print(result)
# result = html.xpath('//li[1]/following::*[2]')
# print(result)
# result = html.xpath('//li[1]/following-sibling::*')
# print(result)


# beautiful soup test
# html = '''
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
#         <p class="story">Once upon a time there were three little sisters;and their names were
#             <a href="http://www.baidu.com/01" class="sister" id="link1"><!--Elsie--></a>
#             <a href="http://www.baidu.com/02" class="sister" id="link2">Lacie</a> and
#             <a href="http://www.baidu.com/03" class="sister" id="link3">Tillie</a>;
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)


# beautiful soup test -> find_all
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print()
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
# print()
# print(soup.find_all(attrs={'id': 'list-1'}))
# print()
# print(soup.find_all(id='list-1'))
# print()
# print(soup.find_all(text=re.compile('Foo')))


# beautiful soup test -> find_all
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find(name='ul'))


# beautiful soup test -> find
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print()
# print(soup.select('ul li'))
# print()
# print(soup.select('#list-2 .element'))
# print()
# for ul in soup.select('li'):        # attribute
#     print(ul['class'])
#     print(ul.attrs['class'])
#     print('Get Text:', ul.get_text())
#     print('String:', ul.string)


# pyquery test
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# print(doc('li'))
# print()
# doc = pq(url='http://www.sniper97.cn')  # use url
# print(doc('title'))
# print()
# doc = pq(filename='test.xml')           # use file
# print(doc('li'))
# print()


# pyquery test -> css
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body" id="list-0">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# print(doc('#list-0 .list li'))


# pyquery test -> find node
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body" id="list-0">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# item = doc('ul')
# print(item)
# print()
# lis = item.find('li')   # son node
# print(lis)
# print()
# par = item.parents()     # parents node
# print(par)
# print()
# par = item.parents('.panel-body')     # parent node , only one point
# print(par)
# print()
# node = doc('li')
# print(node.siblings('.element'))       # find brother node


# pyquery test -> find node
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body" id="list-0">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element1"><a href="www.123.com">Foo</li>
#             <li class="element2"><a href="www.123.com">Bar</li>
#             <li class="element3"><a href="www.123.com">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element4"><a href="www.123.com">Foo</li>
#             <li class="element5"><a href="www.123.com">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# item = doc('ul')
# print(item.attr('class'))
# print(item.attr.id)
# item = doc('li')
# print(item.attr('class'))       # can not output attr
# for i in item.items():
#     print(i.attr('class'))      # can output attr
#     print(i.text())              # can output text
#     print(i.html())              # can output html


# # pyquery test -> class handle
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body" id="list-0">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element1"><a href="www.123.com">Foo</li>
#             <li class="element2"><a href="www.123.com">Bar</li>
#             <li class="element3"><a href="www.123.com">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element4"><a href="www.123.com">Foo</li>
#             <li class="element5"><a href="www.123.com">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# ul = doc('ul')
# print(ul)
# print()
# ul.add_class('action')
# print(ul)
# print()
# ul.remove_class('action')
# print(ul)
# print()


# pyquery test -> attribute handle
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body" id="list-0">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element1"><a href="www.123.com">Foo</li>
#             <li class="element2"><a href="www.123.com">Bar</li>
#             <li class="element3"><a href="www.123.com">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element4"><a href="www.123.com">Foo</li>
#             <li class="element5"><a href="www.123.com">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# ul = doc('ul')
# print(ul)
# print()
# ul.attr('name', 'sniper')
# print(ul)
# print()
# ul.text('change item')
# print(ul)
# print()
# ul.html('<a href="www.123.com">')
# print(ul)
# print()


# pyquery test -> attribute handle
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body" id="list-0">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element1"><a href="www.123.com">Foo</li>
#             <li class="element2"><a href="www.123.com">Bar</li>
#             <li class="element3"><a href="www.123.com">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element4"><a href="www.123.com">Foo</li>
#             <li class="element5"><a href="www.123.com">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# doc = pq(html)
# li = doc('li:first-child')
# print(li)
# print()
# li = doc('li:last-child')
# print(li)
# print()
# li = doc('li:nth-child(2)')
# print(li)
# print()
# li = doc('li:gt(2)')
# print(li)
# print()
# li = doc('li:nth-child(2n)')
# print(li)
# print()
# li = doc('li:contains(Bar)')
# print(li)
# print()
