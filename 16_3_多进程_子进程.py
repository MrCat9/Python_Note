# -*- coding: utf-8 -*-
# 摘自 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000

# 很多时候，子进程并不是自身，而是一个外部进程。
# 我们创建了子进程后，还需要控制子进程的输入和输出。
# subprocess模块可以让我们非常方便地启动一个子进程，
# 然后控制其输入和输出。

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


"""
$ nslookup www.python.org
服务器:  cache-fz.fj133165.com
Address:  58.22.96.66

非权威应答:
名称:    dualstack.python.map.fastly.net
Addresses:  2a04:4e42:1a::223
          151.101.108.223
Aliases:  www.python.org

Exit code: 0

"""
