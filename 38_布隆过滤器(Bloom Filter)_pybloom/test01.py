# -*- coding: utf-8 -*-
# https://github.com/jaybaird/python-bloomfilter
# 下载 bitarray  https://www.lfd.uci.edu/~gohlke/pythonlibs/#bitarray

"""
安装：
1.将pybloom拷贝到工程目录下
2.pip install [工程目录+bitarray-0.8.3-cp36-cp36m-win_amd64.whl]
"""

# from pybloom import BloomFilter
# BloomFilter
#
#
# url = 'https://www.testurl.com'
#
# # f = BloomFilter(capacity=1000000000, error_rate=0.001)
# f = BloomFilter(capacity=100000, error_rate=0.001)
# print(f.capacity)  # 100000
#
# print(len(f))  # 0
# print(url in f)  # False
#
# add_result = f.add(url)
# print(add_result)  # 成功添加返回False
# print(len(f))  # 1
# print(url in f)  # True
#
# add_result = f.add(url)
# print(add_result)  # 添加失败返回True
# print(len(f))  # 1


#


from pybloom import ScalableBloomFilter
# ScalableBloomFilter


url = 'https://www.testurl.com'

# 可变长度
sbf = ScalableBloomFilter(mode=ScalableBloomFilter.LARGE_SET_GROWTH)

print(sbf.capacity)  # 0

print(len(sbf))  # 0
print(url in sbf)  # False

add_result = sbf.add(url)
print(add_result)  # 成功添加返回False
print(len(sbf))  # 1
print(url in sbf)  # True
print(sbf.capacity)  # 100

add_result = sbf.add(url)
print(add_result)  # 添加失败返回True
print(len(sbf))  # 1
print(sbf.capacity)  # 100


#


# from pybloom import ScalableBloomFilter
# import multiprocessing
# # ScalableBloomFilter测试
#
#
# # 全局变量，主进程与子进程是并发执行的，他们不能共享全局变量(子进程不能改变主进程中全局变量的值)
# sbf = ScalableBloomFilter(mode=ScalableBloomFilter.LARGE_SET_GROWTH)
# # list1 = []
#
#
# def add_url(list1):
#     for i in range(10):
#         add_result = sbf.add(i)
#         if not add_result:
#             list1.append(i)
#         print(i, len(sbf), sbf.capacity, list1)
#
#
# if __name__ == '__main__':
#     # 共享变量list1
#     list1 = multiprocessing.Manager().list([])
#
#     print('begin', len(sbf), sbf.capacity)  # begin 0 0
#     print(list1)  # []
#     pool = multiprocessing.Pool(processes=4)  # 4个进程
#     for j in range(16):
#         pool.apply_async(func=add_url, args=(list1, ))
#     pool.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#     pool.join()
#     print('========end========')
#     print('result', len(sbf), sbf.capacity)  # result 0 0
#     print(len(list1), list1)
#     # 40 [0, 1, 2, 3, 0, 4, 1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
