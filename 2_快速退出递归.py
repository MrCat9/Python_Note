# -*- coding: utf-8 -*-

def fan(login_message):
    login_message = login_message[1:]
    print("fan1111=",login_message)

    if login_message.__len__() != 6:    #__len__()返回int
        print("!=")
        return fan(login_message)    #用return快速退出递归

    print("fan2222=",login_message)


if __name__ == "__main__":
    fan("12345678999999")
    print("finish")
