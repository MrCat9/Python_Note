# -*- coding:utf-8 -*-

if __name__ == '__main__':
    print("===方法1开始===")
    list1 = ['111', '1111']
    for a in list1:
        print("no", list1.index(a)+1, "=", a)
    print("===方法1结束===")

    print()

    print("===方法2开始===")
    list2 = ['222', '2222']
    print(list(enumerate(list2)))
    for i,x in enumerate(list2):
        print("no", i+1, "=", x)
    print("===方法2结束===")


"""
===方法1开始===
no 1 = 111
no 2 = 1111
===方法1结束===

===方法2开始===
[(0, '222'), (1, '2222')]
no 1 = 222
no 2 = 2222
===方法2结束===
"""
