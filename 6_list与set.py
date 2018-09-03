# -*- coding: utf-8 -*-

if __name__ == "__main__":
    
    new_list = ["1", "2", "3", "4", "1"]
    old_list = ["1", "2", "3"]
    sub_list = []
    sub_list = list(set(new_list) - set(old_list))
    print(sub_list)    #['4']
    print(sub_list.__class__)    #<class 'list'>
    
    print(set(new_list))    #{'1', '4', '2', '3'}
    print(set(new_list).__class__)    #<class 'set'>
