# 文件介绍

```
my_src.py  要加密的源码
encrypt_src_to_so.py  加密源码
use_my_src.py  调用源码
```




# 使用

```
在工程目录下
执行cmd命令
python my_src.py build_ext

将生成 build 文件夹和 my_src.c 文件
\工程目录\build\lib.win-amd64-3.6\my_src.cp36-win_amd64.pyd
是加密好的文件

将 my_src.cp36-win_amd64.pyd 放到工程目录下，删除 my_src.py（python源码）
运行 use_my_src.py
运行成功
```

