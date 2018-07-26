# -*- coding:utf-8 -*-
import json
import csv
import pymongo
from redis import StrictRedis

# json test -> read
# str = '''
# [{
#     "name": "Sniper",
#     "gender": "male"
#     },{
#     "name": "spider",
#     "gender": "male"
#     }]
# '''
# data = json.loads(str)
# print(data)
# print(data[0]['name'])
# print(data[0].get('age'))


# json test -> output to file
# str = '''
# [{
#     "name": "Sniper",
#     "gender": "male"
#     },{
#     "name": "spider",
#     "gender": "male"
#     }]
# '''
# with open('file/json/data.json', 'w') as file:
#     file.write(json.dumps(str,ensure_ascii=False))


# csv test -> write
# with open('file/csv/data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', '20'])
#     writer.writerows([['10002', 'Bob', '22'], ['10003', 'Jordan', '24']])


# csv test -> write with dic
# with open('file/csv/data.csv', 'w', newline='') as f:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10004', 'name': 'Davie', 'age': '26'})


# csv test -> load file
# with open('file/csv/data.csv', 'r' ,encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# mongodb test -> read
# client = pymongo.MongoClient(host='localhost', port=27017)  # connect to DB
# db = client.quiz                # choose DB
# collection = db.quizzes         # choose collection
# result = collection.find_one({'quiz': '我国历史上第一部编年体史书是？'})   # find data
# print(result)


# Redis test
# redis = StrictRedis(host='localhost', port=6379, db=0, password='')
# redis.set('name', 'Bob')
# print(redis.get('name'))
