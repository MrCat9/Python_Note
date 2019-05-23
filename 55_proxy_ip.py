# -*- coding: utf-8 -*-
# 配合使用 https://github.com/qiyeboy/IPProxyPool
# 需先开启代理IP的服务


import requests
import json
from random import sample


def get_proxy_ip(url_str):
    """
    获取代理IP
    返回一个 tuple  (ip, port)
    :param url_str: 代理IP接口
    :return: (ip, port)  <class 'tuple'>
    """
    r = requests.get(url_str)
    ip_list = json.loads(r.text)  # 会返回多个代理IP
    ip_port = sample(ip_list, 1)  # 从多个代理IP中随机选1个
    ip = ip_port[0][0]
    port = str(ip_port[0][1])
    return ip, port


if __name__ == '__main__':
    # 获取代理ip
    url_str = 'http://127.0.0.1:8000/?type=0&country=国内&count=10'  # types  0: 高匿  1: 匿名  2: 透明
    ip, port = get_proxy_ip(url_str)

    # ip, port = ('114.55.236.62', '3128')

    # 使用代理ip
    proxies = {
        'http': 'http://%s:%s' % (ip, port),
        'https': 'http://%s:%s' % (ip, port)
    }
    r = requests.get('http://httpbin.org/ip', proxies=proxies)
    print(r.text)

