# -*- coding: utf-8 -*-


from selenium import webdriver
import requests


# selenium 
CHROMEDRIVER_EXECUTABLE_PATH = 'F:/chromedriver_win32/chromedriver.exe'
SELENIUM_IMPLICITLY_WAIT = 10

# requests
REQUESTS_TIMEOUT = 10


def selenium_get_url(url, browser=None):
    try:
        use_def_browser = False  # 是否使用方法内创建的浏览器
        # 传参时，没有 browser 的话，将使用该方法内部创建的浏览器，将在该方法最后关闭浏览器，不返回 browser
        # 传参时，传入 browser 的话，将使用外部传入的浏览器，该方法将不会关闭传入的浏览器，返回 browser
        # 建议使用外部浏览器  # 注意在外部关闭浏览器

        if not browser:  # 创建浏览器
            # 更改旗标
            use_def_browser = True

            # 设置浏览器
            chrome_options = webdriver.ChromeOptions()

            # 设置无界面浏览
            # chrome_options.set_headless(True)

            # 浏览器
            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_EXECUTABLE_PATH, chrome_options=chrome_options)  # chromedriver.exe 的路径
            browser.maximize_window()  # 窗口最大化
            browser.implicitly_wait(SELENIUM_IMPLICITLY_WAIT)  # 隐式等待。如果找到，就继续执行，如果没找到就等待10s

        # 请求网页
        browser.get(url)

        # # 切换到新打开的页面
        # current_window = browser.current_window_handle
        # all_handles = browser.window_handles
        # for handle in all_handles:
        #     if handle != current_window:
        #         browser.switch_to.window(handle)

        html_str = browser.page_source

        if not use_def_browser:
            return html_str, browser
        else:
            return html_str
    except Exception as e:
        print(str(e))
    finally:
        if browser and use_def_browser:
            browser.quit()


def requests_get_url(url, params={}, headers={}, proxies={}, timeout=REQUESTS_TIMEOUT):
    # ================================ 请求网页 ================================
    response = requests.get(url=url, params=params, headers=headers, proxies=proxies, timeout=timeout)
    html_str = response.text
    # ==========================================================================

    # ================================ 设置网页编码 ================================
    charset = requests.utils.get_encodings_from_content(html_str)  # 从html的meta中抽取
    '''
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    '''
    if not charset:
        charset = response.apparent_encoding  # apparent_encoding 返回真实编码  # 由程序分析出编码
    response.encoding = charset
    html_str = response.text
    # ==============================================================================

    return html_str


if __name__ == '__main__':
    # # 设置浏览器
    # chrome_options = webdriver.ChromeOptions()
    #
    # # 设置无界面浏览
    # # chrome_options.set_headless(True)
    #
    # # 浏览器
    # browser = webdriver.Chrome(executable_path=CHROMEDRIVER_EXECUTABLE_PATH,
    #                            chrome_options=chrome_options)  # chromedriver.exe 的路径
    # browser.maximize_window()  # 窗口最大化
    # browser.implicitly_wait(SELENIUM_IMPLICITLY_WAIT)  # 隐式等待。如果找到，就继续执行，如果没找到就等待10s

    url = 'https://news.sina.com.cn/roll/'
    # html_str = requests_get_url(url)  # requests
    html_str = selenium_get_url(url)  # selenium 使用内部浏览器
    # html_str = selenium_get_url(url, browser)  # selenium 使用外部浏览器
    print(html_str)

