# -*- coding: utf-8 -*-


import requests
from lxml import etree
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
url = 'http://120.35.30.176/3500/notice/e8d2cd51915e4c338dc1c6ee2f02b127/A3C4095CC579DD7DE05387C115AC8EA5/'
r = requests.get(url, headers=headers).text

selector = etree.HTML(r)
ts = selector.xpath('//table')
for t in ts:
    hs = etree.tostring(t, encoding='utf-8')
    hs = str(hs, encoding='utf-8')
    dfs = pd.read_html(hs)
    for df in dfs:
        print(df)


dfs = pd.read_html(r)
for df in dfs:
    print(df)

