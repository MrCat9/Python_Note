# -*- coding: utf-8 -*-

# 摘自 https://www.jb51.net/article/65497.htm
# https://blog.csdn.net/weixin_41972401/article/details/79991591

import re

# 去除 <> 表示的 html 标签
html = '<a href="//www.jb51.net">脚本之家</a>,Python学习！'
dr = re.compile(r'<[^>]+>', re.S)
dd = dr.sub('', html)
print(dd)  # 脚本之家,Python学习！


# ================================


# 去除 <> 表示的 html 标签
html = 'content: "\u003Cp\u003Egithub Mr.Cat9\u003C\u002Fp\u003E\u003Cp\u003E[this is a test]\u003C\u002Fp\u003Eend"'
print(html)  # content: "<p>github Mr.Cat9</p><p>[this is a test]</p>end"
dr = re.compile(r'<[^>]+>', re.S)
dd = dr.sub('', html)
print(dd)  # content: "github Mr.Cat9[this is a test]end"

# 去除 Unicode 表示的 html 标签
html = r'content: "\u003Cp\u003Egithub Mr.Cat9\u003C\u002Fp\u003E\u003Cp\u003E[this is a test]\u003C\u002Fp\u003Eend"'
print(html)
dr = re.compile(r'\\u003C.+?\\u003E', re.S)
dd = dr.sub('', html)
print(dd)  # content: "github Mr.Cat9[this is a test]end"

