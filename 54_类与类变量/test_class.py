# -*- coding: utf-8 -*-

_py_var = '_py_var'
__py_var = '__py_var'
py_var = 'py_var'


class TestClass:  # class TestClass(object):  # 括号里是 TestClass 类要继承的父类
    _class_var1 = '_class_var1'  # 类变量
    __class_var2 = '__class_var2'
    class_var = 'class_var'

    def __init__(self, arg1, arg2):
        print('执行init方法')
        print(arg1)
        print(arg2)
        self._instance_var1 = '_instance_var1'  # 实例变量
        self.__instance_var2 = '__instance_var2'
        self.instance_var = 'instance_var'

    @staticmethod
    def say_staticmethod(text):  # 类方法  # 没有用到 self 的话建议定义成类方法
        print(text)

    def say(self, text):  # 实例方法  # 要用到 self 的话建议定义成实例方法
        print(text, self)

    def get_class_var1(self):
        print(self._class_var1)
        return self._class_var1

    def get_class_var2(self):
        print(self.__class_var2)
        return self.__class_var2

    def get_class_var(self):
        print(self.class_var)
        return self.class_var

    #

    def get_instance_var1(self):
        print(self._instance_var1)
        return self._instance_var1

    def get_instance_var2(self):
        print(self.__instance_var2)
        return self.__instance_var2

    def get_instance_var(self):
        print(self.instance_var)
        return self.instance_var



