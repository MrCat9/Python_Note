# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", user="···", passwd="···", db="···", charset="utf8")  # 连接数据库
cursor = conn.cursor()

sql = "SELECT restaurant_id, restaurant_name FROM ···"
cursor.execute(sql)
# restaurants_tuple = cursor.fetchall()  # tuple
# db_list = []
# for restaurant in restaurants_tuple:
#     # restaurant_id = restaurant[0]
#     # restaurant_name = restaurant[1]
#     restaurant = restaurant[1] + "(" + restaurant[0] + ")"
#     db_list.append(restaurant)
#     print(restaurant)

db_list = [row[1] + "(" + row[0] + ")" for row in cursor.fetchall()]
for restaurant in db_list:
    print(restaurant)
