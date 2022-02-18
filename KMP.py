# -*- coding: utf-8 -*-
# 模式匹配


def get_index_of_s_in_p(s: str, p: str) -> list:
    """
    采用朴素的字符串匹配算法查找子字符串
    :param s:主字符串
    :param p:匹配模式字符串，子字符串
    :return:匹配成功的所有位置
    """
    len_s = len(s)
    len_p = len(p)
    if len_s < len_p:
        return [-1]

    result_list = []

    for i in range(len_s - len_p + 1):
        for j in range(len_p):
            if s[i + j] == p[j]:
                if j == len_p - 1:
                    result_list.append(i)
                continue  # 字符相等时用continue跳过break
            break

    if result_list:
        return result_list
    else:
        return [-1]


def kmp(s: str, p: str) -> list:
    """
    模式匹配KMP算法
    :param s: 主串
    :param p: 模式串
    :return: 
    """
    len_s = len(s)
    len_p = len(p)
    if len_s < len_p:
        return [-1]

    result_list = []

    def get_next_list(p_str: str) -> list:
        """
        输入模式串，获得next数组
        :param p_str:模式串
        :return:
        """
        p_str_len = len(p_str)

        next_l = [-1] * p_str_len  # next数组用-1初始化
        ii = 0  # next[ii]，同时也是模式串的指针
        jj = -1  # 计算k，next[ii]=k
        while ii < p_str_len - 1:  # 因为第一项等于0
            if jj == -1 or p_str[ii] == p_str[jj]:
                ii += 1  # 匹配成功，指针+1，继续匹配
                jj += 1  # 匹配成功，k值+1
                next_l[ii] = jj
            else:
                jj = next_l[jj]  # 匹配不成功，使用next数组更新指针，继续匹配

        return next_l

    next_list = get_next_list(p)

    i = 0
    j = 0
    while i < len_s:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]

        if j == len_p:
            result_list.append(i - j)  # 记录结果
            i = i - j + 1  # 重置指针，匹配下一个结果
            j = 0

    return result_list


if __name__ == '__main__':
    test_t = '45'
    test_p = '456'
    # [-1]
    r = get_index_of_s_in_p(test_t, test_p)
    print(r)
    r = kmp(test_t, test_p)
    print(r)
    print('----')

    test_t = '1234545678456'
    test_p = '456'
    # [5, 10]
    r = get_index_of_s_in_p(test_t, test_p)
    print(r)
    r = kmp(test_t, test_p)
    print(r)
    print('----')

    test_t = '456'
    test_p = '456'
    # [0]
    r = get_index_of_s_in_p(test_t, test_p)
    print(r)
    r = kmp(test_t, test_p)
    print(r)
    print('----')

    test_t = '11111'
    test_p = '111'
    # [0, 1, 2]
    r = get_index_of_s_in_p(test_t, test_p)
    print(r)
    r = kmp(test_t, test_p)
    print(r)
    print('----')

