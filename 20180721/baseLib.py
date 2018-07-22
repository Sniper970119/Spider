# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import socket
from urllib.request import HTTPPasswordMgrWithPriorAuth, HTTPBasicAuthHandler, ProxyHandler, build_opener
from urllib.error import URLError, HTTPError
import http.cookiejar, urllib.request
from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urlencode, parse_qs, quote, unquote

# urlopen test
# responce = urllib.request.urlopen('https://www.python.org')
# print(responce.read().decode('utf-8'))
# print(type(responce))
# print(responce.status)
# print(responce.getheaders())
# print(responce.getheader('Server'))


# urlopen-data test
# data = bytes(urllib.parse.urlencode({'word': 'hello'}),encoding= 'utf-8')
# responce = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(responce.read())


# urlopen-timeout test
# responce = urllib.request.urlopen('http://www.google.com', timeout=1)
# print(responce.read())


# urlopen-timeout test with try&except
# try:
#     responce = urllib.request.urlopen('http://www.google.com', timeout=1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# request test
# request = urllib.request.Request('https://python.org')
# responce = urllib.request.urlopen(request)
# print(responce.read().decode('utf-8'))


# request test with factor
# url = 'http://httpbin.org/post'
# headers = {
#     "User-Agent": 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Sniper'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# responce = urllib.request.urlopen(req)
# print(responce.read().decode('utf-8'))


# # Opener test
# username = "admin"
# password = ''
# url = 'http://192.168.0.1/index.asp'

# p = HTTPPasswordMgrWithPriorAuth()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# Proxy test
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)
# try:
#     # responce = opener.open('http://www.sniper97.cn')
#     responce = opener.open('https://python.org')
#     print(responce.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


# Cookies test
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# responce = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)


# Cookies test : save in file
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename) # LWPCookieJar is always ok,they are two style
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# responce = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


# Cookies test : use Cookies
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# responce = opener.open('http://www.baidu.com')
# print(responce.read().decode('utf-8'))


# URLError test
# try:
#     responce = urllib.request.urlopen('https://www.baidu.com')
# except URLError as e:
#     print(e.reason)


# HTTPError test
# try:
#     responce = urllib.request.urlopen('http://www.baidu.com')
# except HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')


# urlparse test
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)


# urlunparse test
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))


# urlsplit test
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result, sep='\n')


# urlunsplit test
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))


# urlencode test
# params = {
#     'name': 'Sniper',
#     'age': '21'
# }
# base_url = 'http://www.baidu.com?'
# url = base_url+urlencode(params)
# print(url)


# parse_qs test
# query = '?name=Sniper&age=21'
# print(parse_qs(query))


# quote test
# keyword = '一个不会玩狙的天才狙击手'
# url = 'https://www.baidu.com/s?wd='+quote(keyword)
# print(url)


# unquote test
# url = 'https://www.baidu.com/s?wd=%E4%B8%80%E4%B8%AA%E4%B8%8D%E4%BC%9A%E7%8E%A9%E7%8B%99%E7%9A%84%E5%A4%A9%E6%89%8D%E7%8B%99%E5%87%BB%E6%89%8B'
# print(unquote(url))


