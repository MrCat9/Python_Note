# -*- coding: utf-8 -*-
# 用子进程开进程池

import os
import multiprocessing
import time


def fun(i):
    print(i, 'start')
    time.sleep(2)
    print(i, 'end')


def multi_process_task(i):
    try:
        fun(i)
    except Exception as e:
        print(str(e))
        print('================')


def child_process():
    print('Child process %s.' % os.getpid())
    pool = multiprocessing.Pool(processes=20)  # 4个进程
    # 迭代出每一个结果公告的url
    for i in range(100):
        # print(i)
        pool.apply_async(func=multi_process_task, args=(i, ))
    pool.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    pool.join()
    print('Child process end.')


def parent_process():
    print('Parent process %s.' % os.getpid())
    p = multiprocessing.Process(target=child_process)
    print('Child process will start.')
    p.start()
    print('Parent process end.')


if __name__ == '__main__':
    parent_process()
