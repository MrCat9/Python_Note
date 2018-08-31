# -*- coding: utf-8 -*-

if __name__ == "__main__":

    list1 = ["111", "222", "333", "444", "555"]
    print(list1)    #['111', '222', '333', '444', '555']
   
    a = list1.pop()    #取出最后一个，并从list中删除
    print(a)    #555
    print(list1)    #['111', '222', '333', '444']
    
    list1.append(a)    #添加到最后一个
    print(list1)    #['111', '222', '333', '444', '555']

    for b in list1:    #从第一个开始取
        print(b)    #
    print(list1)    #['111', '222', '333', '444', '555']
