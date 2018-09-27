# -*- coding: utf-8 -*-

# 整理自 http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

import requests

import json


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
}

    # 百度
#     url = "https://www.baidu.com"
    
    # json
#     url = "https://api.github.com/events"
    
    # 图片
#     url = ""


if __name__ == "__main__":
    # http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
    
    # r = requests.get('https://api.github.com/events')
    # r = requests.post('http://httpbin.org/post', data = {'key':'value'})
    # r = requests.put('http://httpbin.org/put', data = {'key':'value'})
    # r = requests.delete('http://httpbin.org/delete')
    # r = requests.head('http://httpbin.org/get')
    # r = requests.options('http://httpbin.org/get')
    
    
#     >>> payload = {'key1': 'value1', 'key2': 'value2'}
#     >>> r = requests.get("http://httpbin.org/get", params=payload)
#     >>> print(r.url)
#     http://httpbin.org/get?key2=value2&key1=value1
    
    
    
#     >>> payload = {'key1': 'value1', 'key2': 'value2'}
#
#     >>> r = requests.post("http://httpbin.org/post", data=payload)
#     >>> print(r.text)
#     {
#       ...
#       "form": {
#         "key2": "value2",
#         "key1": "value1"
#       },
#       ...
#     }
    
    

    
    
    
    
    
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "http://10.10.1.10:1080",
# }
#
#
#                    url      头（cookies放头里）  post的数据  设置代理
# r = requests.post(url=url, headers=headers, data=payload, proxies=proxies)
# 
# 
# print(r)    # <Response [200]>
# print(r.status_code)    # 状态码  #int
# print(r.url)    # 访问的url 
# print(r.text)    # 响应内容
# print(r.content)    # 二进制响应    # 图片
    
    
    
    

    
    
    
    
# # 代理
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "http://10.10.1.10:1080",
# }
# 
# requests.get("http://example.org", proxies=proxies)
    
    
    
    
#     # 下载图片
#     url = ""
#     r = requests.get(url=url, headers=headers)
#     with open("test.webp", "wb") as f:
#         f.write(r.content)
#         f.close()
    
    
    
    
#     # json
#     r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
#     if (r.status_code == requests.codes.ok):
#         print(r.headers['content-type'])
#     commit_data = r.json()
#     print(commit_data)
#     print(commit_data["sha"])
    
#     # json
#     url = "https://api.github.com/events"
#     r = requests.get(url=url, headers=headers)
#     r_json = json.loads(r.text)
#     print(r_json)
#     for a in r_json:
#         print(a['id'])




#     # cookies
#     url = "https://www.baidu.com"
#     r = requests.get(url=url, headers=headers)
#     print(r.cookies["BAIDUID"])
#     print(r.cookies)
#     for cookie in r.cookies:
#         print(cookie)
    
    
    
    
#     # 重定向
#     url = "http://www.baidu.com"
#     r = requests.get(url=url, headers=headers)
#     print(r.url)    # https://www.baidu.com/
#     print(r.status_code)    # 200
#     print(r.history)    # [<Response [302]>]
#     
#                                                 #禁止重定向 
#     r = requests.get('http://github.com', allow_redirects=False)
#     print(r.url)    # http://github.com/
#     print(r.status_code)    # 301
#     print(r.history)    # []
    
    
    
    
#     # 超时时间
#     try:
#         requests.get('http://github.com', timeout=5)
#     except Exception as e:
#         print(e)
#     r = requests.get('https://github.com', timeout=None)    # 永远等待
    
    
    
    
    pass
