# -*- coding: utf-8 -*-
# 通过 selenium 获取 cookie

from selenium import webdriver


def get_cookie(url):
    # 设置浏览器
    chromeOptions = webdriver.ChromeOptions()

    # 设置无界面浏览
    chromeOptions.set_headless(True)

    # 浏览器
    browser = webdriver.Chrome(executable_path="F:/chromedriver_win32/chromedriver.exe",
                                chrome_options=chromeOptions)  # chromedriver.exe 的路径
    browser.maximize_window()  # 窗口最大化

    browser.get(url)

    list_cookies = browser.get_cookies()

    cookie_str = ''
    for cookie in list_cookies:
        cookie_name = cookie.get('name', '')
        cookie_value = cookie.get('value', '')
        cookie_str = cookie_str + '{}={}; '.format(cookie_name, cookie_value)

    return cookie_str


if __name__ == '__main__':
    cookie_str = get_cookie('https://www.baidu.com')
    print(cookie_str)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Cookie': cookie_str,
    }
    print(headers)

