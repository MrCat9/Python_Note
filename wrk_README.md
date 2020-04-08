# 压测工具wrk

https://github.com/wg/wrk

## 安装

```
git clone https://github.com/wg/wrk.git  
cd wrk  
make  
```

### 可能遇到的问题

#### collect2: fatal error: cannot find 'ld'

##### 现象

    ```
    [notroot@testserver wrk]$ make
    Building LuaJIT...
    make[1]: 进入目录“/home/notroot/temp_test01/wrk/obj/LuaJIT-2.1.0-beta3”
    ==== Building LuaJIT 2.1.0-beta3 ====
    make -C src
    make[2]: 进入目录“/home/notroot/temp_test01/wrk/obj/LuaJIT-2.1.0-beta3/src”
    HOSTLINK  host/minilua
    collect2: 致命错误：找不到‘ld’
    编译中断。
    make[2]: *** [host/minilua] 错误 1
    make[2]: 离开目录“/home/notroot/temp_test01/wrk/obj/LuaJIT-2.1.0-beta3/src”
    make[1]: *** [src/luajit] 错误 2
    make[1]: 离开目录“/home/notroot/temp_test01/wrk/obj/LuaJIT-2.1.0-beta3”
    make: *** [obj/lib/libluajit-5.1.a] 错误 2
    ```

##### 解决

1. 查找`ld`

    ```
    [notroot@testserver wrk]$ which ld
    which: no ld in (/usr/...)
    ```
    
    发现没有`ld`

2. 查找`binutils`

    ```
    [notroot@testserver wrk]$ sudo find / | grep binutils
    ```
    
    发现有`binutils`

3. 重装`binutils`

    ```
    [notroot@testserver wrk]$ yum reinstall binutils
    ```

4. 重新编译
    
    ```
    [notroot@testserver wrk]$ make
    ```

## 使用

```
[notroot@testserver wrk]$ ./wrk -t12 -c100 -d30s http://www.baidu.com  
Running 30s test @ http://www.baidu.com
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.70ms   19.38ms 527.69ms   97.83%
    Req/Sec   311.59     73.41   424.00     81.67%
  52500 requests in 30.02s, 779.76MB read
  Socket errors: connect 0, read 32663, write 5, timeout 0
Requests/sec:   1749.01
Transfer/sec:     25.98MB
```

### 参数解释

* 12 threads and 100 connections:

    总共是`12`个线程，`100`个连接(不是一个线程对应一个连接)。

* latency和Req/Sec:

    代表单个线程的统计数据，latency代表延迟时间，Req/Sec代表单个线程每秒完成的请求数，他们都具有平均值，标准偏差，最大值，正负一个标准差占比。一般我们来说我们主要关注平均值和最大值。标准差如果太大说明样本本身离散程度比较高。有可能系统性能波动很大。

* 52500 requests in 30.02s, 779.76MB read

    在`30.02s`之内总共有`52500`个请求，总共读取`779.76MB`的数据

* Socket errors: connect 0, read 32663, write 5, timeout 0

    总共有`32663`个读错误，`0`个超时。
    
* Requests/sec和Transfer/sec

    所有线程平均每秒钟完成了1749.01个请求,每秒钟读取25.98MB数据量。

## 测试本地http

### 启动

```
[notroot@testserver wrk]$ ./wrk http://0.0.0.0:80808/flask_test
Running 10s test @ http://0.0.0.0:80808/flask_test
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     9.79ms    1.11ms  27.05ms   78.34%
    Req/Sec   511.20     13.91   540.00     88.00%
  10176 requests in 10.00s, 6.16MB read
Requests/sec:   1017.23
Transfer/sec:    630.80KB
```

### web后端日志分析

```
# -*- coding: utf-8 -*-

i = 0
with open('app_run.log') as f:
    ls = f.readlines()
    for _l in ls:
        if _l.startswith('2020-04-07'):
            print(_l)
            i += 1
print(i)  # 10188  # 后台接收到10188条请求
```

## 参考

HTTP压测工具之wrk https://www.jianshu.com/p/ac185e01cc30
