# -*- coding: utf-8 -*-

from selenium import webdriver
from fake_useragent import UserAgent


user_agent = UserAgent()  # 使用随机UA头

# 设置浏览器
chromeOptions = webdriver.ChromeOptions()

# 设置无界面浏览
# chromeOptions.set_headless(True)

# 设置 user_agent
random_ua = user_agent.random
print(random_ua)
chromeOptions.add_argument('user-agent={}'.format(random_ua))

# 设置代理 IP
ip = '114.55.236.62'
port = '3128'
chromeOptions.add_argument("--proxy-server=http://{0}:{1}".format(ip, port))
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152

# 浏览器
browser = webdriver.Chrome(executable_path="F:/chromedriver_win32/chromedriver.exe", chrome_options=chromeOptions)  # chromedriver.exe 的路径
browser.maximize_window()  # 窗口最大化
browser.implicitly_wait(5)  # 隐式等待。如果找到，就继续执行，如果没找到就等待10s

browser.get('http://httpbin.org/user-agent')
# browser.get('http://news.baidu.com/')

# 切换到新打开的页面
# current_window = browser.current_window_handle
# all_handles = browser.window_handles
# for handle in all_handles:
#     if handle != current_window:
#         browser.switch_to.window(handle)

print(browser.page_source)


browser.get('http://httpbin.org/ip')
print(browser.page_source)


browser.quit()

