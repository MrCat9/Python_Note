# python源码保护与打包

Python打包成exe https://mp.weixin.qq.com/s/yV9bP-bvrm-D96uwVfpSTA
python文件或文本加密 https://blog.csdn.net/ccweb/article/details/86655226

## pyc  容易被破解

pyc_test.py 下

```python
# -*- coding: utf-8 -*-

import py_compile


py_compile.compile(r'F:\pycharm\···\test01.py')  # py文件完整的路径
```

## 打包成exe

### pyinstaller

cmd 下，cd到.py文件的文件夹

```
pyinstaller test01.py
```

### Nuitka

https://zhuanlan.zhihu.com/p/133303836

## 编译成 .pyd 文件（windows上） 或 .so文件（Linux上）

### cython

将 python 源码 .py 文件转为 .pyd 文件 或 .so文件
```
https://mp.weixin.qq.com/s?__biz=MzAxMjUyNDQ5OA==&mid=2653559171&idx=2&sn=e44ec05bf8619fcc8976e0d5e49589c1&chksm=806e373eb719be28d6fa0e5e74fb464af95d7dc17759d2bc628b62aa29db6ce1ea03081a80a0&mpshare=1&scene=1&srcid=0414jjvOSILGKZIwgbPrAvRR&key=e0570729d1f68810d702c6e52bbc2b627c89093601550bf090c728374381c08bb5e6abc70dec67c71a3cbd9390567ce28a1d801afe1c97ec5f00a4fad75667080299d022a46b3f233bc6a278b90fc8e0&ascene=1&uin=MjI5NTY3NjkwMw%3D%3D&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=q%2BZpM4te0mDMn7vQAA8gI0ol4lqGBrMh42TtE5tRJf2Td3Kb0W59TdbHPBJYHKaQ
https://blog.csdn.net/weixin_44216589/article/details/85203893
```

报错 Cython：Unable to find vcvarsall.bat
```
https://blog.csdn.net/sunlilan/article/details/80040858
https://www.cnblogs.com/yyds/p/7065637.html
```

查看 python MSC
cmd下
```
C:\Users\admin>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

```
CPython 解释器 与 VC 编译器版本对应关系
https://blog.51cto.com/walkerqt/2089935
https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B#Internal_version_numbering
```

```
详见 encrypt_src_test
```

