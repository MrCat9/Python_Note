# -*- coding: utf-8 -*-

_test_class_var = '_test_class_var'
__test_class_var = '__test_class_var'


class TestClass:  # class TestClass(object):  # 括号里是 TestClass 类要继承的父类
    _class_var1 = '_class_var1'
    __class_var2 = '__class_var2'
    class_var = 'class_var'

    def __init__(self, arg1, arg2):
        print('执行init方法')
        print(arg1)
        print(arg2)

    def say(self, text):
        print(text)

    def get_class_var1(self):
        print(self._class_var1)
        return self._class_var1

    def get_class_var2(self):
        print(self.__class_var2)
        return self.__class_var2



