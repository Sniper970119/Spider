# -*- coding:utf-8 -*-
from pymongo import MongoClient
from config import *


class Mongo():
    def __init__(self, host=MONGO_HOST, port=MONGO_PORT):
        self.client = MongoClient(host=host, port=port)
        self.db = self.client.Test
        self.collection = self.db.WeiXin

    def insert(self, result):
        print(result)
        self.collection.insert(result)
