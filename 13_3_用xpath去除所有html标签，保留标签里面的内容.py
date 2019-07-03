# -*- coding: utf-8 -*-


from lxml import etree


html = '<a href="//www.jb51.net">脚本之家</a>,Python学习！'
selector = etree.HTML(text=html)
text = selector.xpath('string()')
print(text)  # 脚本之家,Python学习！
