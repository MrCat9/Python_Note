# -*- coding: utf-8 -*-

import pyperclip  # python 操作剪切板
from selenium import webdriver
# import time
import os


# pyperclip.copy('aaa')  # 向剪切板写入 aaa
clipboard_str = pyperclip.paste()  # 读取剪切板内容
print(clipboard_str)

browser = webdriver.Ie(executable_path='F:\iedriver\IEDriverServer.exe')
browser.implicitly_wait(10)  # 隐式等待
url = 'http://www.baidu.com'
# url = 'https://www.baidu.com/s?ie=UTF-8&wd=python'
browser.get(url)
# time.sleep(1)  # 强制等待
# keyword = 'test：你好，世界123'
browser.find_element_by_css_selector('input[id="kw"]').send_keys(clipboard_str)  # 输入
browser.find_element_by_css_selector('input[id="su"]').click()  # 点击
# time.sleep(10)
# browser.close()

print('结束进程 IEDriverServer.exe')
os.system('taskkill /im IEDriverServer.exe /f')  # 结束进程 (python执行cmd)
# /im : 根据进程名
# /f : 强制结束
