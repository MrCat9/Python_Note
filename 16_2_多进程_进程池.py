# -*- coding: utf-8 -*-
# 摘自 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.close()
    p.join()
    print('All subprocesses done.')


"""
Parent process 9964.
Waiting for all subprocesses done...
Run task 0 (2816)...
Run task 1 (14248)...
Run task 2 (2336)...
Run task 3 (8108)...
Task 2 runs 0.36 seconds.
Run task 4 (2336)...
Task 0 runs 0.72 seconds.
Task 3 runs 0.93 seconds.
Task 1 runs 1.63 seconds.
Task 4 runs 2.67 seconds.
All subprocesses done.

"""
