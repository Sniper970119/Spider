# -*- coding:utf-8 -*-
import requests
from lxml import etree


class Login():
    def __init__(self):
        self.headers = {
            'referer': 'https://github.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password
        }
        self.session.post(self.post_url, data=post_data, headers=self.headers)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//*[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//*[@id="user_profile_blog"]/@value')[0]
        print(name, '\n', email)


if __name__ == "__main__":
    login = Login()
    login.login(email='359366783@qq.com', password='000000')
