# -*- coding: utf-8 -*-


if __name__ == '__main__':
    list1 = [6, 1, 2, 7, 3, 4, 5]

    print(sorted(list1))  # sorted() 有返回值，返回排序后的新list，原list不变  # sorted 接受的参数为所有可迭代对象  # [1, 2, 3, 4, 5, 6, 7]
    print(str(list1))  # [6, 1, 2, 7, 3, 4, 5]
    
    print(list1.sort())  # sort() 无返回值，是对原list排序，不生成新的list  # sort 是list的方法  # None
    print(list1)  # [1, 2, 3, 4, 5, 6, 7]
