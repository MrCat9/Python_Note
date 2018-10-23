# -*- coding:utf-8 -*-

if __name__ == '__main__':
    num = 100
    list1 = [x*3 for x in range(1, int(num/3)+1) if x*3 <= num]
    print(list1)


