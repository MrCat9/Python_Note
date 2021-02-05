# -*- coding: utf-8 -*-


import re


def rm_whitespace(s: str, mode='split_join') -> str:
    """
    去除字符串中的空白符（空格/制表符/换行）
    :param s: 输入字符串
    :param mode: 选择模式
                'split_join': 速度快
                're_sub': 使用正则
                're_sub2': 使用正则，较re_sub快
    :return:
    """

    new_s = s

    if mode == 'split_join':
        new_s = ''.join(s.split())
    elif mode == 're_sub':
        new_s = re.sub(r'\s|\t|\n', '', s)
    elif mode == 're_sub2':
        new_s = re.sub(r'\s', '', s)
    return new_s


if __name__ == '__main__':
    test_s = '''你好，这是一段测试文本。后面是两个空格  然后是一个制表符	最后是换行，这是换行开始

这是换行结束
测试结束'''
    print(test_s)
    print('-' * 16)
    r = rm_whitespace(test_s)
    print(r)
