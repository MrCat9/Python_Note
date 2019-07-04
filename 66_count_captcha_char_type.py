# -*- coding: utf-8 -*-


import os
from collections import Counter
import matplotlib.pyplot as plt


if __name__ == '__main__':
    dir_path = 'png_data'

    all_captcha_str = ''
    images_list = os.listdir(dir_path)
    # print(images_list)
    for image_name in images_list:

        captcha = image_name.replace('.png', '')  # 取出文件名中的验证码

        all_captcha_str += captcha
    # print(all_captcha_str)

    counter = Counter()
    for char in all_captcha_str:
        counter[char] = counter[char] + 1

    print(counter)
    print(len(counter))

    # for k, v in counter.items():
    #     print(k, v)

    # for k in counter.keys():
    #     print(k)

    # for v in counter.values():
    #     print(v)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.bar(counter.keys(), counter.values())

    plt.show()
