# -*- coding: utf-8 -*-

from pymongo import MongoClient


conn = MongoClient('127.0.0.1', 27017)
db = conn.test_database  # 连接test_database数据库，没有则自动创建
my_collection = db.test_collection  # 使用test_collection集合，没有则自动创建


def save_data_to_db(data_dict):
    my_collection.insert(data_dict)


if __name__ == '__main__':
    data_dict = {'name': 'zhangsan', 'age': 18, 'other': {'sex': 'M', 'from': 'CN'}}
    save_data_to_db(data_dict)
