# -*- coding: utf-8 -*-
# 摘自 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000

import time
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    time.sleep(3)
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    name = 'test'
    p = Process(target=run_proc, args=(name,))
    print('Child process will start.')
    # 用start()方法启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    # p.join()
    print('Child process end.')


# 有用join()方法的话，打印如下：
"""
Parent process 13384.
Child process will start.
Run child process test (7256)...
Child process end.

"""


# 没用join()方法的话，打印如下：
"""
Parent process 5712.
Child process will start.
Child process end.
Run child process test (12064)...

"""
