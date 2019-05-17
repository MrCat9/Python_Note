# -*- coding: utf-8 -*-
# https://www.cnblogs.com/bw13/p/6549248.html


import requests


# ================================ 请求网页 ================================
url = 'https://www.chinanews.com/gn/2019/05-16/8837888.shtml'
params = {}
headers = {}
proxies = {}
timeout = 10
response = requests.get(url=url, params=params, headers=headers, proxies=proxies, timeout=timeout)
html_str = response.text
# ==========================================================================
print(html_str)  # 编码前

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
print(html_str)  # 编码后

