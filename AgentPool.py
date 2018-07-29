# -*- coding:utf-8 -*-
import redis
from random import choice

# save
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        print('''
        初始化 地址、端口、密码
        ''')
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        print('''
        添加代理，设置最高分数''')
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, proxy)

    def random(self):
        print('''
        随机获取有效代理''')
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                print('代理池为空')

    def decrease(self, proxy):
        print('''
        代理值减一分''')
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        print('''
        判断是否存在''')
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        print('''
        将代理设置为最大值''')
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        print('''
        获取数量''')
        return self.db.zcard(REDIS_KEY)

    def all(self):
        print('''
        获取全部代理''')
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
