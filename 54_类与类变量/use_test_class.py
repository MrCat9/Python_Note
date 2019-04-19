# -*- coding: utf-8 -*-

from test_class import TestClass
from test_class import _py_var
from test_class import __py_var
from test_class import py_var


if __name__ == '__main__':
    print(_py_var)  # _py_var
    print(__py_var)  # __py_var
    print(py_var)  # py_var

    #
    
    # 类调用类变量
    print(TestClass._class_var1)  # _class_var1
    # print(TestClass.__class_var2)  # 报错
    print(TestClass.class_var)  # class_var
    
    # 类调用类方法
    TestClass.say_staticmethod('class_hello')  # hello  # 类直接调用类方法时，需要给类方法传参数
    # 类调用实例方法
    TestClass.say(None, 'class_hello')  # hello  # 类直接调用实例方法时，也需要给 self 传参数

    #

    test = TestClass('arg1', 'arg2')
    '''
    执行init方法
    arg1
    arg2
    '''
    
    # 实例调用类变量
    print(test._class_var1)  # _class_var1
    # print(test.__class_var2)  # 报错
    print(test.class_var)  # class_var
    
    # 实例调用实例变量
    print(test._instance_var1)  # _instance_var1
    # print(test.__instance_var2)  # 报错
    print(test.instance_var)  # instance_var

    # 实例调用类方法
    test.say_staticmethod('hello')  # hello  # 类的实例对象调用类方法（静态方法）时，不会将实例本身传给第一个参数
    # 实例调用实例方法
    test.say('hello')  # hello  # 类的实例对象调用实例方法时，会将对象本身自动传给第一个参数（一般实例方法的第一个参数是 self）

    test.get_class_var1()  # _class_var1
    test.get_class_var2()  # __class_var2
    test.get_class_var()  # class_var
    test.get_instance_var1()  # _instance_var1
    test.get_instance_var2()  # __instance_var2
    test.get_instance_var()  # instance_var



