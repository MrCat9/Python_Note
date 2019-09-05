# python_notes 记录一些有关python的笔记

python 文档 https://docs.python.org/3.6/index.html




## 目录




1_selenium在add_cookie之前要先get




2_快速退出递归可以考虑return和yield




3_从list中取出元素

```
pop,append,for
```




4_写文件(w,wb)读文件(r,rb)

```python
# w下write()中的变量为str

# wb下write()中的变量为byte

with open("test.json", "w") as f:
        f.write(json_doc)
```

```python
# 文件里都是英文的话r,rb都行

# 文件里有中文的话用r会报错，用rb不会

with open("test.json", "r") as f:
        doc = json.load(f)
```




5_全局变量要在某个方法内对其进行修改时，要用global

```
在方法中修改全局变量时，需在方法中用 global 声明变量；
只是读全局变量的话则不需要声明。
```




6_set可以对一个list去重，可以让两个list相减，得到差集




7_ HTTP状态码




8_geohash2




9_selenium设置无界面浏览，设置user-agent，设置代理ip




10_list的指针问题




11_对dict的list去重

根据dict中的某一key的value，对dict的list去重，value相同视为重复




12_requests




13_用re去除所有html标签，保留标签里面的内容

```
75_w3lib 比 re 好用
```




13_2_用re匹配出img标签，再匹配出img标签中的图片url




13_3_用xpath去除所有html标签，保留标签里面的内容

```
xpath 效果比 re 好
```




14_re报错bad character range




15_插入到sql中的数据包含单引号（'）时，应将一个单引号（'）改成两个单引号（''）

str1 = str1.replace("'", "''")




16_进程和线程

父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

16_8_多进程_多线程补充
```
多进程(multiprocessing)  https://www.cnblogs.com/smallmars/p/7093603.html
多线程(threading)  https://www.cnblogs.com/smallmars/p/7149507.html
多CPU，多核，多进程，多线程  http://www.cnblogs.com/csfeng/p/8670704.html
GIL全局锁  https://www.cnblogs.com/hukey/p/7263207.html
```

16_9_用子进程开进程池




17_从数据库中取出数据，转为list




18_验证码识别(pytesseract)




19_一款入门级的人脸、视频、文字检测以及识别的项目




20_ORM_sqlalchemy（用于操作数据库）

20_2_ORM_sqlalchemy（外键）

20_3_ORM_sqlalchemy_外键




21_列表生成式

列出100以内3的倍数




22_获取list元素下标




23_合并dict




24_解决报错_'latin-1' codec can't encode characters in position




25_url的编码与解码

```python
urllib.parse.quote()
urllib.parse.quote_plus()

urllib.parse.unquote()
urllib.parse.unquote_plus()
```



26_执行命令行，获取命令行打印的信息

```python
# -*- coding: utf-8 -*-

import os

command = 'ping www.baidu.com '  # 可以直接在命令行中执行的命令
r = os.popen(command)  # 执行该命令
text = r.read()  # 命令行打印的信息

print(text)
```




27_日志logging

```python
# -*- coding: utf-8 -*-
# 摘自 https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial

import logging

if __name__ == '__main__':
    logging.basicConfig(filename='log_examp.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
```




28_python源码保护




29_django读取不在工程目录下的图片




30_django登录验证




31_django 404，500的全局配置




32_发送邮件
```
https://blog.csdn.net/qq_20417499/article/details/80566265
```




33_最大限度切分字符串（考虑顺序）
```
"123"
['123', '1', '12', '23', '2', '3']
```




34_编写docx




35_pdf转png




36_python操作文件文件夹




37_selenium获取cookie




38_布隆过滤器(Bloom Filter)_pybloom




39_python分布式(BaseManager)




40_python获取CPU使用率，内存使用率，网络使用状态

```
https://blog.csdn.net/bubu8633/article/details/8258342
```




41_python搭建简单的web服务器实现资源文件共享

cmd 下
```
λ python -m http.server 8888
Serving HTTP on 0.0.0.0 port 8888 (http://0.0.0.0:8888/) ...
```
```
https://blog.csdn.net/u014762921/article/details/79064756/
```



42_生成器(generator)(yield)

```
https://blog.csdn.net/SL_World/article/details/86507872
```




43_python异步IO之协程(yield)(yield from)(async)

```
https://blog.csdn.net/SL_World/article/details/86597738
https://blog.csdn.net/SL_World/article/details/86691747
```




43_2_网络并发库

```
greenlet
eventlet
gevent

Python协程
https://zhu327.github.io/2016/06/16/python%E5%8D%8F%E7%A8%8B/

Python eventlet 模块笔记
https://blog.csdn.net/u010827484/article/details/81223035

class eventlet.Timeout 可以向任何东西添加超时，在 timeout 秒后抛出异常

廖雪峰 gevent
https://www.liaoxuefeng.com/wiki/897692888725344/966405998508320

gevent 官网
http://www.gevent.org/index.html
```




44_selenium操作ie_python操作剪切板_python执行cmd.py

```
ie driver 下载：
http://selenium-release.storage.googleapis.com/index.html

Selenium IE webdriver 常见问题：
https://www.jianshu.com/p/3ee5587ee364
https://blog.csdn.net/u013061459/article/details/77145215

Selenium+Python调用IE浏览器：
https://www.cnblogs.com/leeboke/p/5013793.html
```




45_python操作MongoDB

```
python操作MongoDB
https://www.cnblogs.com/melonjiang/p/6536876.html
```

```
开启MongoDB

F:\mongodb\bin
λ mongod -dbpath "F:\mongoDB\data\db"
```

```
MongoDB数据导入与导出
https://www.cnblogs.com/qingtianyu2015/p/5968400.html

F:\mongodb\bin
λ mongoexport -d test_database -c test_collection -o C:\Users\admin\Desktop\test.json --type json
```




46_python去除字符串中的\x20_\xa0_\t_\n

```
75_w3lib 更好用
```

```python
# -*- coding: utf-8 -*-

str1 = '你好\x20啊\xa0啊\t啊\n啊'
print(str1)
# 你好 啊 啊	啊
# 啊

str1 = ''.join(str1.split())
print(str1)
# 你好啊啊啊啊
```




47_selenium_find_element_note

```
find_element_by_xpath
find_element_by_id
find_element_by_class_name
find_element_by_tag_name
```




48_selenium_使用随机UA头




49_Python3操作Elasticsearch

```
Python3操作Elasticsearch进行增删改查  https://blog.csdn.net/weixin_42126327/article/details/81285487
```




50_newspaper3k设置useragent_proxies_headers

50_2_将外部请求下来的html源码给newspaper解析

可以给外部的请求加 useragent,proxies 等

```
news.download(input_html=html_str)
```




51_re_正则匹配网页源码中的_日期时间（新闻发布时间）




52_装饰器

```
https://blog.csdn.net/qq_42156420/article/details/81169554
```




53_urllib

```
url 拼接
解析 url 的 Host
```




54_类与类变量




55_免费IP代理池

```
https://github.com/qiyeboy/IPProxyPool
```




56_tushare_股票数据

```
https://github.com/waditu/tushare
http://tushare.org/
```




57_requests乱码(encoding)




58_re（正则表达式）去除部分html标签

```
75_w3lib 更好用
```




59_request_tool

```
包括 selenium 和 requests 两种get url的方法
```




60_itertools_排列组合




61_列表list和字典dict的迭代

```
https://www.cnblogs.com/wangbin2188/p/6532510.html
```




62_list排序




63_map_reduce_方法

```
from functools import reduce
map()
reduce()
https://www.liaoxuefeng.com/wiki/897692888725344/989703124920288
```




64_collections

```
collections是Python内建的一个集合模块，提供了许多有用的集合类。
https://www.liaoxuefeng.com/wiki/897692888725344/973805065315456

模块内有 tuple list dict 的子类，当原来的 tuple list dict 不好用的时候可以试试

namedtuple  可命名的 tuple
deque  高效实现插入和删除操作的双向列表
defaultdict  带默认值的dict，引用不存在的key时返回默认值，不会报错
OrderedDict  有序的dict
Counter 计数器
```




65_验证码手动标记




66_验证码字符种类统计




67_with

```
https://blog.csdn.net/lxy210781/article/details/81176687
```




68_向python程序里传参数




69_设置最大递归深度

```
python 最大递归次数 RuntimeError: maximum recursion depth exceeded
https://blog.csdn.net/tangwenbo124/article/details/72822692

import sys
sys.setrecursionlimit(10000)  # set the maximum depth as 10000
```




70_python_whl

```
对于pip安装不了的包可以考虑用whl安装
https://www.lfd.uci.edu/~gohlke/pythonlibs/
```




71_requirements

```
requirements.txt 可以同时 pip install 多个包

python requirements.txt使用
https://www.jianshu.com/p/9402a6818f86
```




72_四舍五入

```
https://www.cnblogs.com/xieqiankun/p/the_truth_of_round.html
```




73_hashlib_摘要算法

```
MD5  SHA1
https://www.liaoxuefeng.com/wiki/897692888725344/923057313018752
```




74_twisted与deferred对象

```
https://www.cnblogs.com/xianguang/p/7027661.html
```




75_w3lib

```
https://w3lib.readthedocs.io/en/latest/w3lib.html
encoding Module
html Module
http Module
url Module
去除html标签  去除空格，换行符，制表符  网页降噪
```

```python
import w3lib.html

html_str = w3lib.html.remove_comments(html_str)  # 去除注释
# html_str = w3lib.html.remove_tags(html_str, which_ones=('style', ))  # 去除 style 标签
html_str = w3lib.html.remove_tags_with_content(html_str, which_ones=('style', ))  # 去除 style 标签及其内容

str1 = '你好\x20啊\xa0啊\t啊\n啊'
str1 = w3lib.html.replace_escape_chars(str1, which_ones=('\n', '\t', '\r', '\x20', '\xa0'), replace_by='/')
print(str1)  # 你好/啊/啊/啊/啊
```

