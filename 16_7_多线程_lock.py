# -*- coding: utf-8 -*-
# 摘自 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192823818768cd506abbc94eb5916192364506fa5d000

# 如果我们要确保balance计算正确，就要给change_it()上一把锁，
# 当某个线程开始执行change_it()时，我们说，
# 该线程因为获得了锁，因此其他线程不能同时执行change_it()，
# 只能等待，直到锁被释放后，获得该锁以后才能改。
# 由于锁只有一个，无论多少线程，
# 同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。
# 创建一个锁就是通过threading.Lock()来实现

import threading


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000000):
        # 先要获取锁:
        lock.acquire()
        # 用try...finally来确保锁一定会被释放
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


# 假定这是你的银行存款:
balance = 0

lock = threading.Lock()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)  # 0

