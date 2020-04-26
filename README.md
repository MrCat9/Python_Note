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

https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0014021031294178f993c85204e4d1b81ab032070641ce5000

https://www.cnblogs.com/Zzbj/p/10212279.html

sqlalchemy实现时间列自动更新 https://blog.csdn.net/kuangshp128/article/details/85700701

sqlalchemy更新数据 https://blog.51cto.com/12965094/2362002?source=dra

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



42_迭代器(Iterator)生成器(generator)(yield)

```
https://blog.csdn.net/SL_World/article/details/86507872
```




43_python异步IO之协程(yield)(yield from)(async)(asyncio)

```
https://segmentfault.com/a/1190000008814676

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




#### [51_re_正则匹配网页源码中的_日期时间（新闻发布时间）](https://github.com/MrCat9/Python_Note/blob/master/parser_tool.py)




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




#### [59_request_tool](https://github.com/MrCat9/Python_Note/blob/master/request_tool.py)

```
包括 selenium 和 requests 两种get url的方法
```




#### 60_itertools_排列组合




#### 61_列表list和字典dict的迭代

```
https://www.cnblogs.com/wangbin2188/p/6532510.html
```




#### 62_list排序




#### 63_map_reduce_方法

```
from functools import reduce
map()
reduce()
https://www.liaoxuefeng.com/wiki/897692888725344/989703124920288
```




#### 64_collections

https://www.liaoxuefeng.com/wiki/897692888725344/973805065315456

```
collections是Python内建的一个集合模块，提供了许多有用的集合类。

模块内有 tuple list dict 的子类，当原来的 tuple list dict 不好用的时候可以试试

namedtuple  可命名的 tuple
deque  高效实现插入和删除操作的双向列表
defaultdict  带默认值的dict，引用不存在的key时返回默认值，不会报错
OrderedDict  有序的dict
Counter 计数器
```

#### [64_2_使用Counter统计list中每种元素的个数](https://github.com/MrCat9/Python_Note/blob/master/list_element_count.py)




#### [65_验证码手动标记](https://github.com/MrCat9/Python_Note/blob/master/captcha_mark.py)




#### 66_验证码字符种类统计




#### 67_with

```
https://blog.csdn.net/lxy210781/article/details/81176687
```




#### 68_向python程序里传参数




#### 69_设置最大递归深度

```
python 最大递归次数 RuntimeError: maximum recursion depth exceeded
https://blog.csdn.net/tangwenbo124/article/details/72822692

import sys
sys.setrecursionlimit(10000)  # set the maximum depth as 10000
```




#### 70_python_whl

对于pip安装不了的包可以考虑用whl安装

https://pypi.org/simple/

https://www.lfd.uci.edu/~gohlke/pythonlibs/




#### 71_requirements

```
requirements.txt 可以同时 pip install 多个包

生成
pip freeze > requirements.txt

安装
pip install -r requirements.txt
```

> python requirements.txt使用  https://www.jianshu.com/p/9402a6818f86




#### 72_四舍五入

```
https://www.cnblogs.com/xieqiankun/p/the_truth_of_round.html
```




#### 73_hashlib_摘要算法

```
MD5  SHA1
https://www.liaoxuefeng.com/wiki/897692888725344/923057313018752
```




#### 74_twisted与deferred对象

```
https://www.cnblogs.com/xianguang/p/7027661.html
```




#### [75_w3lib](https://github.com/MrCat9/Python_Note/blob/master/w3lib_test.py)

w3lib库文档 https://w3lib.readthedocs.io/en/latest/w3lib.html

```
encoding Module
html Module
http Module
url Module
去除html标签  去除空格，换行符，制表符  去除html实体（如：&nbsp; &rdquo; &mdash; 等）  网页降噪
```




#### 76_phone库

Python(phone)模块获取手机号归属地、区号、运营商等 https://www.cnblogs.com/yaoqian/p/9358107.html




#### 77_pipenv

https://www.jianshu.com/p/d08a4aa0008e
        



#### 78_操作gif图

```
# 使用模块 imageio
imageio.mimread  # 读取gif，每一帧会存放到list的一个位置中
imageio.mimsave  # 保存gif，输入也是一个list数组
```




#### 79_PIL.Image和np.ndarray图片与Tensor之间的转换

https://blog.csdn.net/tsq292978891/article/details/78767326




#### 79_dlib

```
Windows下安装
pip install xxx.whl

Linux下安装
pip install dlib
```

dlib 官网 http://dlib.net/

dlib 文件下载 http://dlib.net/files/

人脸识别之Python DLib库进行人脸关键点识别 https://www.cnblogs.com/raorao1994/p/11001755.html

用Python实现简单的人脸相似度对比 https://blog.csdn.net/m0_38106923/article/details/83862334




#### 80_Python执行JS代码

https://blog.csdn.net/ychgyyn/article/details/90112448




#### 81_Python转js

https://blog.csdn.net/baozhourui/article/details/88058450




#### 82_selenium打开本地的html文件

```python
browser = webdriver.Chrome()
browser.get('file:///'+os.path.abspath('test.html'))  # os.path.abspath()方法可以获取文件的绝对路径
```




#### 83_让IE浏览器运行js时，不再提示“允许阻止内容”
https://blog.csdn.net/u010682330/article/details/77531028




#### 84_python字符串前的加符号的含义

python中 r'', b'', u'', f'' 的含义 https://blog.csdn.net/qq_35290785/article/details/90634344




#### 85_python生成二维码

https://github.com/sylnsfar/qrcode/blob/master/README-cn.md




#### 86_face_recognition

https://github.com/ageitgey/face_recognition

```
人脸检测  人脸识别

安装：
1. 先安装dlib
2. pip install face_recognition
```




#### 87_LabelImg

https://github.com/tzutalin/labelImg

```
Labelimg 是一个图形图像标注工具，用于在图像中标注物体边界框
```




#### 88_图像数据增强(Data Augmentation)

Augmentor https://github.com/mdbloice/Augmentor

Data Augmentation--数据增强解决你有限的数据集 https://blog.csdn.net/u010801994/article/details/81914716

非常好用的Python图像增强工具，适用多个框架 https://blog.csdn.net/u011984148/article/details/99439562

图像数据增强 https://www.cnblogs.com/siyuan1998/p/10686616.html

图像数据增强方法一览 https://segmentfault.com/a/1190000016526917




#### 89_bunch

pypi bunch https://pypi.org/project/bunch/

python函数——Bunch配置加载 https://blog.csdn.net/wcy23580/article/details/89708801

```
Bunch is a dictionary that supports attribute-style access, a la JavaScript.
```

```python
>>> b = Bunch()
>>> b.hello = 'world'
>>> b.hello
'world'
```




#### 90_汉字unicode编码范围

https://blog.csdn.net/gywtzh0889/article/details/71083459/




#### 91_PIL将png的RGBA四通道改为jpg的RGB三通道方法

https://blog.csdn.net/missyougoon/article/details/85331493

```python
img = Image.open('test.png')
img = img.convert('RGB')
```

```
PIL包含九种不同模式：1，L，P，RGB，RGBA，CMYK，YCbCr,I，F
使用Image.convert()，可以在这九中模式中进行切换。
模式1为二值图像，非黑即白。
模式L为灰度图像。
RGB就是通常说的三原色。
RGBA就是上例上的在三原色的基础上增加了一个alpha通道。
```




#### 92_用*和**给函数传参

```python
def foo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
```

https://www.cnblogs.com/beiluowuzheng/p/8461518.html




#### 93_Faker

```
Faker is a Python package that generates fake data for you.
生成随机姓名、地址、电子邮箱等随机用户信息
```

https://github.com/joke2k/faker

https://pypi.org/project/Faker/

https://faker.readthedocs.io/en/master/locales/zh_CN.html




#### 94_爬虫js加密

python爬虫js加密解密系列文章合集 https://blog.csdn.net/weixin_33933118/article/details/89551449




#### 95_通用新闻正文解析

newspaper https://github.com/codelucas/newspaper

GeneralNewsExtractor https://github.com/kingname/GeneralNewsExtractor

利用文本及符号密度来提取新闻网页正文 https://pylist.com/t/1576112934




#### 96_通用论坛解析

https://spaces.ac.cn/archives/4422

https://blog.csdn.net/qq_34202873/article/details/78452449




#### 97_图片格式转换.ppm转.jpg

```python
from PIL import Image

img = Image.open('input_img.ppm')
img.save('output_img.jpg')
img.show()
```




#### [98_取出字符串str中的特定字符](https://github.com/MrCat9/Python_Note/blob/master/find_str_char.py)

```
取出字符串中的所有数字/所有数字和字母
```




#### 99_字符串str根据字典替换

```python
t = str.maketrans('lzZoODpq', '12200099')  # dict
r = 'olz345678q'.translate(t)  # str
print(r)  # 0123456789
```

```python
t = {
    ord('l'): '1',
    ord('z'): '2',
    ord('Z'): '2',
    ord('o'): '0',
    ord('O'): '0',
    ord('D'): '0',
    ord('p'): '9',
    ord('q'): '9',
}
# ord()
# Return the Unicode code point for a one-character string.
# 返回单个字符的 Unicode 值（int）
r = 'olz345678q'.translate(t)  # str
print(r)  # 0123456789
```




#### [100_使用正则表达式re完成字符串str根据字典替换](https://github.com/MrCat9/Python_Note/blob/master/str_dict_replace.py)

http://www.cocoachina.com/articles/88965




#### 101_re_sub_正则表达式sub替换

https://blog.csdn.net/qq_43088815/article/details/90214217?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

http://www.mamicode.com/info-detail-2327645.html




#### 102_openpyxl读写excel

https://www.cnblogs.com/programmer-tlh/p/10461353.html




#### 103_package和模块

https://www.jianshu.com/p/178c26789011




#### 104_Python中的__all__

```
__all__是一个字符串list，用来定义模块中对于from XXX import *时要对外导出的符号，即要暴露的接口，但它只对import *起作用，对from XXX import XXX不起作用。
```

https://www.jianshu.com/p/ca469f693c31




#### 105_找出列表list中的重复元素

https://blog.csdn.net/August1226/article/details/82144759

```python
from collections import Counter  # 引入Counter
a = [29, 36, 57, 12, 79, 43, 23, 56, 28, 11, 14, 15, 16, 37, 24, 35, 17, 24, 33, 15, 39, 46, 52, 13]
b = dict(Counter(a))
print([key for key, value in b.items() if value > 1])  # 只展示重复元素
print({key: value for key, value in b.items() if value > 1})  # 展现重复元素和重复次数
```




#### 106_思知机器人

```
聊天机器  知识图谱
```

https://www.ownthink.com

https://github.com/ownthink/KnowledgeGraphData




#### 107_对字典dict按value排序

https://www.cnblogs.com/beile/p/11276532.html

```python
d = {
    '1': 1,
    '5': 5,
    '3': 3,
    '2': 2,
    '4': 4,
}
r = sorted(d.items(), key=lambda x: x[1], reverse=True)  # reverse=True -> 降序排列
print(r)
```




#### [108_wrk_压力测试性能测试工具](https://github.com/MrCat9/Python_Note/blob/master/wrk_README.md)

https://github.com/wg/wrk

HTTP压测工具之wrk https://www.jianshu.com/p/ac185e01cc30




#### 109_python高性能web框架

```
Tornado
Japronto
```




#### 110_locust_压力测试性能测试工具

https://github.com/locustio/locust

性能测试工具Locust的使用 https://www.cnblogs.com/ailiailan/p/9474973.html




#### 111_selenium_chromedriver

http://chromedriver.storage.googleapis.com/index.html

chromedriver与chrome各版本及下载地址  https://blog.csdn.net/cz9025/article/details/70160273




#### 112_fake_user_agent

```
fake ua
```

[fake_ua.json](https://github.com/MrCat9/Python_Note/blob/master/fake_ua.json)

```python
import json


with open('fake_ua.json', 'r') as f:
    a = json.loads(f.read())
```




#### 113_splash

```
splash是一个javascript渲染服务，支持异步。考虑用来替换selenium。
将selenium集成到scrapy时会造成堵塞，降低scrapy异步框架的性能，所以考虑用支持异步的splash替换selenium。
```

scrapy-splash https://github.com/scrapy-plugins/scrapy-splash

python3之Splash https://www.cnblogs.com/zhangxinqi/p/9279014.html

python爬虫之Splash使用初体验 https://www.cnblogs.com/lei0213/p/8432031.html

Python爬虫：splash+requests简单示例 https://blog.csdn.net/mouday/article/details/82843401




#### [114_使用pandas解析html中的table](https://github.com/MrCat9/Python_Note/blob/master/pandas_read_html.py)

```python
dfs = pd.read_html(hs)
```




#### 115_测试框架pytest

https://docs.pytest.org/en/latest/







