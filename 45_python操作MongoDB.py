# -*- coding: utf-8 -*-
# python操作MongoDB: https://www.cnblogs.com/melonjiang/p/6536876.html
# MongoDB导入导出以及数据库备份: https://www.cnblogs.com/qingtianyu2015/p/5968400.html

from pymongo import MongoClient


conn = MongoClient('127.0.0.1', 27017)
db = conn.test_database  # 连接test_database数据库，没有则自动创建
my_collection = db.test_collection  # 使用test_collection集合，没有则自动创建


def save_data_to_db(data_dict):
    my_collection.insert(data_dict)


if __name__ == '__main__':
    data_dict = {
        'name': 'zhangsan',
        'age': 18,
        'other': {
            'sex': 'M',
            'from': 'CN',
        },
        'data': [
            {'code1': 'python', 'year': 1},
            {'code2': 'java'},
        ],
    }
    save_data_to_db(data_dict)
