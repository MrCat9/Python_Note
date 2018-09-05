# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# import temp4




if __name__ == "__main__":
    
    chromeOptions = webdriver.ChromeOptions()
    
    # 设置无界面浏览
    chromeOptions.set_headless(True)
    
    
    
    ip = "115.154.170.4"
    port = "1080"
    
    # 设置代理
    chromeOptions.add_argument("--proxy-server=http://{0}:{1}".format(ip, port))
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    
    browser = webdriver.Chrome(executable_path="F:/chromedriver_win32/chromedriver.exe", chrome_options = chromeOptions)
    browser.maximize_window()    #窗口最大化


    browser.get("http://www.baidu.com")
