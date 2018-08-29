# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import json

# 微博cookies


browser = webdriver.Chrome(executable_path="F:/chromedriver_win32/chromedriver.exe")  # chromedriver.exe 的路径
browser.get("https://weibo.com/")
time.sleep(7)  #延迟7s再执行下面的语句  #执行太快可能导致页面还没加载完毕，就执行selector，导致找不到 id="loginname"
browser.find_element_by_css_selector("#loginname").send_keys("···")  #找到id名为loginname的
browser.find_element_by_css_selector("input[node-type='password']").send_keys("···")  #找到node-type='password'的input
captcha = input("输入验证码\n>")
try:
    browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(captcha)
except Exception:
    pass
browser.find_element_by_css_selector("a[tabindex='6'] span").click()  #找到一个tabindex='6'的a标签，之后在这个a标签下找span标签
   
   
time.sleep(5)
   
   
   
list_cookies = browser.get_cookies()
print(list_cookies)
# for dict_cookie in list_cookies:
#     dict_cookie['domain'] = '.weibo.com'
#     del dict_cookie['httpOnly']
# print(list_cookies)
  
json_cookies = json.dumps(list_cookies)
with open('cookies.json', 'w') as f:
    f.write(json_cookies)

# dump-->str
# load-->dict

  
browser = webdriver.Chrome(executable_path="F:/chromedriver_win32/chromedriver.exe")  # chromedriver.exe 的路径
browser.get("https://weibo.com/")    #在add_cookie之前要先get
with open('cookies.json', 'r') as f:
    list_cookies = json.load(f)
for cookie in list_cookies:
    print(cookie)
    browser.add_cookie(cookie)
 
 
browser.get("https://weibo.com/messages?topnav=1&wvr=6")
time.sleep(5)
