# -*- coding: utf-8 -*-
# http://www.cnblogs.com/kongxiaoshuang/p/10174418.html


import requests
import re


# ================================ 请求网页 ================================
url = 'https://www.chinanews.com/gn/2019/05-16/8837888.shtml'
params = {}
headers = {}
proxies = {}
timeout = 10
response = requests.get(url=url, params=params, headers=headers, proxies=proxies, timeout=timeout)
html_str = response.text
# ==========================================================================
# print(html_str)
print(len(html_str))


# ================================ 设置网页编码 ================================
charset = requests.utils.get_encodings_from_content(html_str)  # 从html的meta中抽取
'''
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
'''
if not charset:
    charset = response.apparent_encoding  # apparent_encoding 返回真实编码  # 由程序分析出编码
response.encoding = charset
html_str = response.text
# ==============================================================================
# print(html_str)
print(len(html_str))


# ================================ 去除部分 html 源码中的标签 ================================
re_comment = re.compile('<!--[^>]*-->')  # HTML注释
html_str = re_comment.sub('', html_str)  # 去掉HTML注释  # 去除单行的注释，且注释中的内容不含>
print(len(html_str))

re_script = re.compile('<s*script[^>]*>[^<]*<s*/s*scripts*>', re.I)  # 去除 Script
html_str = re_script.sub('', html_str)
print(len(html_str))

re_style = re.compile('<s*style[^>]*>[^<]*<s*/s*styles*>', re.I)  # style
html_str = re_style.sub('', html_str)  # 去掉 style
print(len(html_str))
# ============================================================================================

