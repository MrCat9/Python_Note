# -*- coding: utf-8 -*-

i = 0

def fun():
    global i
    i = i + 1

if __name__ == "__main__":
    print(i)    # 0
    fun()
    print(i)    # 1
