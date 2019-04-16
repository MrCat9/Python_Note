# -*- coding: utf-8 -*-

from urllib.parse import urljoin

# url 拼接
base_url = 'http://mini.eastday.com/'
url = '//mini.eastday.com/a/190415194204243.html?qid=www.baidu.com&needrec=index_jrdftt&subtype=toutiao&rcgid=5b72e6f024652665&pgnum=1&idx=1&ishot=1&recommendtype=-1&suptop=0&domain=mini&listSoftName=mini&btype1=index_jrdftt&batchid=4b02cbac4120524f'
url = urljoin(base_url, url)  # url 拼接
print(url)  # http://mini.eastday.com/a/190415194204243.html?qid=www.baidu.com&needrec=index_jrdftt&subtype=toutiao&rcgid=5b72e6f024652665&pgnum=1&idx=1&ishot=1&recommendtype=-1&suptop=0&domain=mini&listSoftName=mini&btype1=index_jrdftt&batchid=4b02cbac4120524f


#


from urllib.parse import urlparse

# 解析 url 的 Host
url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1555315202&ver=1547&signature=ZiWq7N-fzvtvkkbbroswRuXrwktymoc2sB6x28eRe6-Z*sjjw*pXIaBkLfCwfGHSl42G16cOKY4ev3QduD4wGgdu1Yg*KiRLnI0fk6IkHvru8HhZ2OTNSjNXMH8WOHYh&new=1'
res = urlparse(url)
# print(res)
host_name = res.netloc
print(host_name)  # mp.weixin.qq.com
print('news' in host_name)  # False

