# -*- coding: utf-8 -*-


import re
# 摘自 http://www.cocoachina.com/articles/88965


d = {
    'ASAP': 'as soon as possible',
    'AFAIK': 'as far as I know',
    'I': 'i',
    'random_str': 'random_str_replace',  # random_str 未出现在要处理的字符串中
}

s = 'I will do this ASAP, AFAIK.  Regards, X'
print(s)
# I will do this ASAP, AFAIK.  Regards, X

r = re.sub(r'(' + '|'.join(d.keys()) + r')', lambda m: d[m.group(0)], s)
print(r)
# i will do this as soon as possible, as far as I know.  Regards, X
