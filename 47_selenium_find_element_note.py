# -*- coding: utf-8 -*-

from selenium import webdriver


# 设置浏览器
chromeOptions = webdriver.ChromeOptions()

# # 设置无界面浏览
# chromeOptions.set_headless(True)

# 浏览器
browser = webdriver.Chrome(executable_path="F:/chromedriver_win32/chromedriver.exe",
                           chrome_options=chromeOptions)  # chromedriver.exe 的路径
browser.maximize_window()  # 窗口最大化
browser.implicitly_wait(5)  # 隐式等待。如果找到，就继续执行，如果没找到就等待10s

# browser.get('http://news.baidu.com/')

# 切换到新打开的页面
# current_window = browser.current_window_handle
# all_handles = browser.window_handles
# for handle in all_handles:
#     if handle != current_window:
#         browser.switch_to.window(handle)

#

# browser.get('http://m.news.cctv.com/2019/03/16/ARTIgLRcomZ4gjlFPYaTDr7I190316.shtml')
# a = browser.find_element_by_id('loginForm')
# # a = a.find_element_by_xpath('div[@id="right"]')  # 在 id="loginForm" 的子标签（只向下一层）中找 id="right" 的div
# a = a.find_element_by_xpath('*[@id="right"]')  # 在 id="loginForm" 的子标签（只向下一层）中找 id="right" 的标签
# a = a.find_element_by_class_name('tn-title')  # 在 id="right" 的标签的所有后代标签中找 class="tn-title" 的标签
# a = a.find_element_by_tag_name('a').click()  # 会找到第一个 a 标签

# browser.get('http://m.news.cctv.com/2019/03/16/ARTIgLRcomZ4gjlFPYaTDr7I190316.shtml')
# a = browser.find_element_by_xpath('//div[@class="function"]/span[@class="shouji"]').click()

# browser.get('http://m.news.cctv.com/2019/03/16/ARTIgLRcomZ4gjlFPYaTDr7I190316.shtml')
# a = browser.find_element_by_xpath('//div[@class="function"]')
# a = a.find_element_by_class_name('shouji')
# a.find_element_by_xpath('a[@title="手机观看"]').click()

browser.get('http://www.jobbole.com/')
a = browser.find_element_by_class_name('the-latest')
aa = a.find_elements_by_tag_name('a')  # elements 可以迭代
for temp in aa:
    print(temp.get_attribute('href'))
print('================')
temp = a.find_element_by_tag_name('a')  # element 不能迭代
print(temp.get_attribute('href'))


browser.quit()
  
