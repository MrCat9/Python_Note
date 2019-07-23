# -*- coding: utf-8 -*-


import sys


argv_list = sys.argv
print(argv_list)
argv_list = argv_list[1:]  # 第一个是.py文件名
print(argv_list)

'''
在 cmd 下
cd 到 .py 文件所在的文件夹

>python temp_test02.py
['temp_test02.py']
[]

>python temp_test02.py argv1 argv2 argv3
['temp_test02.py', 'argv1', 'argv2', 'argv3']
['argv1', 'argv2', 'argv3']
'''

'''
在 pycharm 下
选择 Run -> Edit Configurations... -> 选择要运行的 .py -> Parameters -> 填入参数argv1 argv2 argv3
（填入的参数以空格隔开）
接下来该.py的 run, debug 都将传入这3个参数

运行结果如下
['F:/pycharm/admin/alexnet_test/temp_test02.py', 'argv1', 'argv2', 'argv3']
['argv1', 'argv2', 'argv3']
'''
