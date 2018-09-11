# -*- coding: utf-8 -*-
if __name__ == "__main__":
    list1 = ["1","2","3"]
    print(list1)    #['1', '2', '3']
    list2 = list1
    print(list2)    #['1', '2', '3']
    list2.append("4")
    print(list1)    #['1', '2', '3', '4']
    print(list2)    #['1', '2', '3', '4']
    
    
# 这样写会死循环
#     for a in list1:
#         list2.append(a)
