# python源码保护

## pyc

pyc_test.py 下

```python
# -*- coding: utf-8 -*-

import py_compile


py_compile.compile(r'F:\pycharm\···\test01.py')  # py文件完整的路径
```

## 打包成exe

cmd 下，cd到.py文件的文件夹

```
pyinstaller test01.py
```

## 编译成.so文件

```
详见 encrypt_src_test
```
