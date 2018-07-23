# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import socket
from urllib.request import HTTPPasswordMgrWithPriorAuth, HTTPBasicAuthHandler, ProxyHandler, build_opener
from urllib.error import URLError, HTTPError
import http.cookiejar, urllib.request
from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urlencode, parse_qs, quote, unquote
from urllib.robotparser import RobotFileParser
import requests
import re
from requests import Request, Session

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


# robotparser test
# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))


# requests test
# r = requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)


# requests test -> get
# data = {
#     'name': 'Spider',
#     'age': '21'
# }
# r = requests.get('http://httpbin.org/get',data)
# print(r.text)
# print(r.json()) # 可以用json形式解析返回


# requests test -> zhihu
# headers = {
#     'User-agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4)AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# requests test -> binary file
# r= requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb')as f:
#     f.write(r.content)


# requests test -> post
# data = {
#     'name': 'Spider',
#     'age': '21'
# }
# r= requests.post('http://httpbin.org/post', data=data)
# print(r.text)


# requests test -> responce
# headers = {
#     'User-agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4)AppleWebKit/537.36(KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('http://www.jianshu.com',headers=headers)
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)


# requests test -> post
# files = {
#     'file':open('favicon.ico', 'rb')
# }
# r = requests.post('http://httpbin.org/post',files=files)
# print(r.text)


# requests test -> cookies
# r= requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key+'='+value)


# requests test -> cookies -> zhihu
# headers = {
#     'Cookies': '_xsrf=Buel2ZkWUtC7SgTSB8EJPCF4Br5Rcimr;'
#                ' _zap=1f70cf3c-9b1a-4513-a8f3-d6abb4270880;'
#                ' d_c0="AMCkg9ZJ7w2PTnLDQAncDVfCUc59_P4qggs=|1532176674";'
#                ' q_c1=6e44fd4dd5064217a670c1c5aaf31711|1532176674000|1532176674000;'
#                ' capsion_ticket="2|1:0|10:1532176678|14:capsion_ticket|44:NWQ1YWNkNzU5ZjhiNGJmYmI0NTkyNmJiYzg4OWM5YzM=|67f43de453cf2ec1315e2bc98b734af6bef647447e40c73341943d6a8a2b4724";'
#                ' z_c0="2|1:0|10:1532176688|4:z_c0|92:Mi4xemN3Z0FnQUFBQUFBd0tTRDFrbnZEU1lBQUFCZ0FsVk5NSGRBWEFEVnFndHJQYUZ1OWNXdHJidTJ4eldhX0NkRUFn|8155841af129425202e2ef982f977517d7940a6257866e3df4221696ff4710ef"',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# r= requests.get('https://www.zhihu.com/people/zhao-yu-12-34/activities', headers=headers)
# print(r.text)


# requests test -> session
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r= requests.get('http://httpbin.org/cookies')
# print(r.text)
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# requests test -> verify
# responce = requests.get('https://www.12306.cn', verify=False)
# print(responce.status_code)


# request test -> proxies
# proxies = {
#     'http': 'http://xxx.xxx.xxx.xxx:xxxx',
#     'https': 'https://xxx.xxx.xxx.xxx:xxxx'
# }
# r = requests.get('https://www.taobao.com', proxies=proxies)
# print(r.text)


# requests test -> timeout
# r = requests.get('https://www.taobao.com', timeout=1)
# print(r.text)


# requests test -> auth
# r = requests.get("http://192.168.0.1/index.asp", auth=('admin', ''))
# print(r.status_code)
# print(r.text)


# requests test -> prepare_request
# url = 'http://httpbin.org/post'
# data = {
#     'name': 'Sniper'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)