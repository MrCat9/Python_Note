# -*- coding: utf-8 -*-

def name_separation(name):
    name_list = []
    name_len = name.__len__()
    for i in range(name_len):
        str1 = name[i:]
        name_list.append(str1)
        j = str1.__len__()
        for j in range(1, j):
            str2 = str1[:j]
            name_list.append(str2)
    return name_list

if __name__ == '__main__':
    name = "123"
    print(name)
    name_list = name_separation(name)
    print(name_list)


"""
123
['123', '1', '12', '23', '2', '3']
"""
