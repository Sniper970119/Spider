# -*- coding:utf-8 -*-
import requests
from requests import Session
from SoGouSpider.db import RedisQueue
from SoGouSpider.config import *
from SoGouSpider.request import WeixinRequest
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from requests import ReadTimeout
from MongoDB import Mongo
import re


class Spider():
    base_url = 'http://weixin.sogou.com/weixin'
    key_word = 'RNG'
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection	': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'cookies': 'CXID=0DDCDF3AB524336D02F12EE46CD334E4; SUID=D4C85D7C3965860A5AA39D940000145A; '
                   'IPLOC=CN2102; SUV=1531959792494460; '
                   'sct=5; SNUID=8E67BCEBD1D5A2CE38998221D186284B; '
                   'ld=wyllllllll2bFdo5lllllVH5TZGlllllnLLdflllllwlllll9Zlll5@@@@@@@@@@; '
                   'LSTMV=347%2C155; LCLKINT=4472; ABTEST=0|1531961096|v1; weixinIndexVisited=1; '
                   'JSESSIONID=aaa4Ta7_4rS8e9Jqz3Hsw; '
                   'ppinf=5|1532852075|1534061675|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTclOUYlQjMlRTUlQ'
                   'TQlQjR8Y3J0OjEwOjE1MzI4NTIwNzV8cmVmbmljazoxODolRTclOUYlQjMlRTUlQTQlQjR8dXNlcmlkOjQ0Om85dDJsdUI5VE8'
                   '5TE1CemdVRDd5dC10RjI4MzBAd2VpeGluLnNvaHUuY29tfA; '
                   'pprdig=Lk7HiV8rT2LS8uZh0riBcnZ8cokN-aN-Yv5OjbnX3qmZS4SYIg7PnnZqXWsxfPwNF1M-YxeT9PZQxGVw7qc6d15IjwIg'
                   '_2E9537JOqzdHQL34_9ntlXJ_gYE7RCQ-Nt_piMGk9cvi5Ll9oRWWsdK2dUqWTbDnESGbkA07hWhO9E; '
                   'sgid=06-34211517-AVtdd2sgghdVYlHDIz6Ug1U; ppmdig=153286085500000088c26503f3219f8b3403a4a6915fc676',
        'Host': 'weixin.sogou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }
    session = Session()
    queue = RedisQueue()
    mongo = Mongo()

    def get_proxy(self):
        """
        从代理池获取代理
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query': self.key_word, 'type': 2})
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        print('start:' + str(weixin_request.need_proxy))
        self.queue.add(weixin_request)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_request = WeixinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeixinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            'date': doc('#publish_time').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data

    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
            print(weixin_request.need_proxy)
            if weixin_request.need_proxy:
                # 代理服务器
                proxyHost = "http-dyn.abuyun.com"
                proxyPort = "9020"

                # 代理隧道验证信息
                proxyUser = "H44849JU5O0CUXJD"
                proxyPass = "9D6530023F397B62"

                proxy = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                    "host": proxyHost,
                    "port": proxyPort,
                    "user": proxyUser,
                    "pass": proxyPass,
                }

                print('proxy:' + str(proxy))

                if proxy:
                    proxies = {
                        'http': proxy,
                        'https': proxy
                    }
                    return requests.get(weixin_request.url, proxies=proxies)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False

    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request Failed', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            # weixin_request.need_proxy = True
            print('schedule:' + str(weixin_request.need_proxy))
            callback = weixin_request.callback
            print('Schedule', weixin_request.url)
            response = self.request(weixin_request)
            print('状态码' + str(response.status_code))
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', type(result))
                        if isinstance(result, WeixinRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mongo.insert(result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
