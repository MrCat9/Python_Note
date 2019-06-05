# -*- coding: utf-8 -*-

import itertools

# ================ 组合 ================
list1 = [1, 2, 3, 4]
all_combinations = []
for i in range(1, len(list1)+1):
    iter1 = itertools.combinations(list1, i)
    iter1_list = list(iter1)
    print(iter1_list)
    all_combinations.append(iter1_list)
print(all_combinations)
# [[(1,), (2,), (3,), (4,)], [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)], [(1, 2, 3, 4)]]
# ======================================

print('='*64)

# ================ 排列 ================
print(list(itertools.permutations(list1,2)))
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
# ======================================
