# -*- coding: utf-8 -*-

from urllib import parse

a = "%E4%BD%A0%E5%A5%BD+%E4%BD%A0%E5%A5%BD"
aa1 = parse.unquote(a)
aa2 = parse.unquote_plus(a)
print(aa1)  # 你好+你好
print(aa2)  # 你好 你好


b = "你好  /+"
bb1 = parse.quote(b)
bb2 = parse.quote_plus(b)
print(bb1)  # %E4%BD%A0%E5%A5%BD%20%20/%2B
print(bb2)  # %E4%BD%A0%E5%A5%BD++%2F%2B

