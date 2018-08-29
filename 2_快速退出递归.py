# -*- coding: utf-8 -*-

def fan(login_message):
    login_message = login_message[1:]
    print("fan1111=",login_message)

    if login_message.__len__() != 6:    #__len__()返回int
        print("!=")
        return fan(login_message)    #用return快速退出递归    #函数执行到return就退出

    print("fan2222=",login_message)


if __name__ == "__main__":
    fan("12345678999999")
    print("finish")

"""
##################运行结果##################
fan1111= 2345678999999
!=
fan1111= 345678999999
!=
fan1111= 45678999999
!=
fan1111= 5678999999
!=
fan1111= 678999999
!=
fan1111= 78999999
!=
fan1111= 8999999
!=
fan1111= 999999
fan2222= 999999
finish

############################################
"""





# -*- coding: utf-8 -*-


def fan(login_message):
    login_message = login_message[1:]
    print("fan1111=",login_message)
 
    return check(login_message)
     
    print("fan2222=",login_message)    #没有执行到这段

def check(login_message):
    if login_message.__len__() != 6:    #__len__()返回int
        print("!=")
        return fan(login_message)
     
     
if __name__ == "__main__":
    fan("1234567654321")
    print("finish")

"""
##################运行结果##################
fan1111= 234567654321
!=
fan1111= 34567654321
!=
fan1111= 4567654321
!=
fan1111= 567654321
!=
fan1111= 67654321
!=
fan1111= 7654321
!=
fan1111= 654321
finish

############################################
"""

