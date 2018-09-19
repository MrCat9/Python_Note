# -*- coding: utf-8 -*-
import re

line = "XXX出生于1996年3月21日"

reg_str = ".*出生于(\d{4}[年-/]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"
match_obj = re.match(reg_str,line)
if match_obj:
    print(match_obj.group(1))
# 报错：sre_constants.error: bad character range 年-/ at position 12


# 修改  年-/  为  年/-  就没问题了。
# -*- coding: utf-8 -*-
import re

line = "XXX出生于1996年3月21日"

reg_str = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[月/-]$|$))"
match_obj = re.match(reg_str,line)
if match_obj:
    print(match_obj.group(1))    # 1996年3月21
