# -*- coding: utf-8 -*-

from newspaper import Article
import requests


url = 'https://news.163.com/19/0422/02/EDB8C3NU0001875O.html'
news = Article(url, language='zh')

html_str = requests.get(url).text

news.download(input_html=html_str)
print(html_str == news.html)  # True
news.parse()
text = news.text
title = news.title

print('text:', text)
print('title:', title)

