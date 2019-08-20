# -*- coding: utf-8 -*-


import hashlib


def get_md5(url):  # MD5摘要生成
    if isinstance(url, str):  # python中str == Unicode  # 判断是不是str，其实是判断是不是Unicode，python3中默认是Unicode编码
        url = url.encode(encoding='utf_8')  # 如果是Unicode，则转换成utf-8，哈希只认utf-8
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ == '__main__':
    md5 = get_md5('123')
    print(md5)
