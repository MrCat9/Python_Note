# -*- coding: utf-8 -*-
# 取出字符串str中的特定字符（取出字符串中的所有数字/所有数字和字母）


import re


str1 = 'abc123你def456好ABC'

# ================================================================
char = re.findall(r'[a-z]', str1)
print(char)  # ['a', 'b', 'c', 'd', 'e', 'f']
bigchar = re.findall(r'[A-Z]', str1)
print(bigchar)  # ['A', 'B', 'C']
num = re.findall(r'[0-9]', str1)
print(num)  # ['1', '2', '3', '4', '5', '6']
blank = re.findall(r' ', str1)
print(blank)  # []
chi = re.findall(r'[\u4E00-\u9FFF]', str1)  # \u4E00-\u9FFF是中文的范围
print(chi)  # ['你', '好']
other = len(str1) - len(char) - len(bigchar) - len(num) - len(blank) - len(chi)
print(other)  # 0
num_char = re.findall(r'[0-9]|[a-z]|[A-Z]', str1)
print(num_char)  # ['a', 'b', 'c', '1', '2', '3', 'd', 'e', 'f', '4', '5', '6', 'A', 'B', 'C']
# ================================================================
# 判断字符串是否是数字
print(str1.isdigit())  # False

# 取出字符串中的数字 方法1
num = filter(str.isdigit, str1)
num = list(num)
print(num)  # ['1', '2', '3', '4', '5', '6']

# 取出字符串中的数字 方法2
num = [x for x in str1 if x.isdigit()]
print(num)  # ['1', '2', '3', '4', '5', '6']

# 取出字符串中的字母
num = [x for x in str1 if x.isalpha()]
print(num)  # ['a', 'b', 'c', '你', 'd', 'e', 'f', '好', 'A', 'B', 'C']

# 取出字符串中的数字和字母
num = [x for x in str1 if x.isalnum()]
print(num)  # ['a', 'b', 'c', '1', '2', '3', '你', 'd', 'e', 'f', '4', '5', '6', '好', 'A', 'B', 'C']
# ================================================================

