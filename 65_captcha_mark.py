# -*- coding: utf-8 -*-
# 验证码手动标记


import requests
# import time
from PIL import Image
import matplotlib.pyplot as plt
import os
import datetime


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'User-Agent': get_ua()  # 获取随机 UA头
}


if __name__ == '__main__':
    try:
        os.mkdir('png_data')  # 创建单个目录
    except Exception as e:
        print(str(e))

    url = ''
    for i in range(1000):
        print(i)
        # time.sleep(3)

        # ======== 下载图片 ========
        r = requests.get(url=url, headers=headers)
        # with open('png_data/{}.png'.format(i), 'wb') as f:
        with open('png_data/temp.png', 'wb') as f:
            f.write(r.content)
            f.close()
        # ==========================

        # ======== 显示图片 ========
        img = Image.open('png_data/temp.png')
        plt.figure('temp')
        plt.imshow(img)
        plt.show()
        # ==========================

        # ======== 输入验证码 ========
        name = input('输入验证码：')
        # ============================

        # ======== 文件重命名 ========
        time_str = str(datetime.datetime.now().strftime('%Yy%mm%dd_%Hh%Mm%Ss'))
        os.rename('png_data/temp.png', 'png_data/{}__{}.png'.format(name, time_str))
        # ============================

