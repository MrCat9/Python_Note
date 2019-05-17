# -*- coding: utf-8 -*-

# 摘自 https://www.jb51.net/article/65497.htm
# https://blog.csdn.net/weixin_41972401/article/details/79991591

import re
html='<a href="//www.jb51.net">脚本之家</a>,Python学习！'
dr = re.compile(r'<[^>]+>',re.S)
dd = dr.sub('',html)
print(dd)    # 脚本之家,Python学习！
