# -*- coding: utf-8 -*-


from collections import Counter

list1 = [1, 2, 3, 4, 1]
list1_c = Counter(list1)
print(list1_c)  # Counter({1: 2, 2: 1, 3: 1, 4: 1})
