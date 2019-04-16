# -*- coding: utf-8 -*-

from test_class import TestClass
from test_class import _test_class_var
from test_class import __test_class_var


if __name__ == '__main__':
    test = TestClass('arg1', 'arg2')
    '''
    执行init方法
    arg1
    arg2
    '''
    print(test._class_var1)  # _class_var1
    # print(test.__class_var2)  # 报错
    print(test.class_var)  # class_var

    print(_test_class_var)  # _test_class_var
    print(__test_class_var)  # __test_class_var

    test.say('hello')  # hello
    test.get_class_var1()  # _class_var1
    test.get_class_var2()  # __class_var2

