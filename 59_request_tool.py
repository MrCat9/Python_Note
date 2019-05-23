# -*- coding: utf-8 -*-


from selenium import webdriver
import requests


from settings import CHROMEDRIVER_EXECUTABLE_PATH, SELENIUM_IMPLICITLY_WAIT
from settings import REQUESTS_TIMEOUT


# # selenium
# CHROMEDRIVER_EXECUTABLE_PATH = 'F:/chromedriver_win32/chromedriver.exe'
# SELENIUM_IMPLICITLY_WAIT = 10
#
# # requests
# REQUESTS_TIMEOUT = 10


def requests_init():
    params = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        # 'User-Agent': get_ua()  # 获取随机 UA头
    }

    # ip, port = get_proxy_ip()  # 获取随机 代理IP
    # ip, port = ('116.196.81.58', '3128')
    # proxies = {
    #     'http': 'http://{}:{}'.format(ip, port),
    #     'https': 'http://{}:{}'.format(ip, port),
    # }
    proxies = {}  # 不使用代理

    timeout = REQUESTS_TIMEOUT

    return params, headers, proxies, timeout


def requests_get_url(url):
    # ================================ 生成 requests 的 get 方法的参数 ================================
    params, headers, proxies, timeout = requests_init()  # 可在 requests_init 方法中写 获取随机UA头，代理IP
    # =================================================================================================

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
        charset = [response.apparent_encoding]  # apparent_encoding 返回真实编码  # 由程序分析出编码
    response.encoding = charset[0]
    html_str = response.text
    # ==============================================================================

    return html_str


def selenium_init():
    # 获取随机 UA头
    user_agent = None

    # 获取随机 代理IP
    ip_port = None

    # ================================ 浏览器 ================================
    # 设置浏览器
    chrome_options = webdriver.ChromeOptions()

    # 设置无界面浏览
    # chrome_options.set_headless(True)

    # 设置 user_agent
    if user_agent:
        chrome_options.add_argument('user-agent={}'.format(user_agent))

    # 设置代理 IP
    if ip_port:
        # ip = '114.55.236.62'
        # port = '3128'
        ip, port = ip_port
        chrome_options.add_argument("--proxy-server=http://{0}:{1}".format(ip, port))
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152

    # 浏览器
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_EXECUTABLE_PATH,
                               chrome_options=chrome_options)  # chromedriver.exe 的路径
    browser.maximize_window()  # 窗口最大化
    browser.implicitly_wait(SELENIUM_IMPLICITLY_WAIT)  # 隐式等待。如果找到，就继续执行，如果没找到就等待10s
    # ========================================================================

    return browser


def selenium_get_url(url, browser=None):
    use_def_browser = False  # 是否使用方法内创建的浏览器
    # 传参时，没有 browser 的话，将使用该方法内部创建的浏览器，将在该方法最后关闭浏览器，不返回 browser
    # 传参时，传入 browser 的话，将使用外部传入的浏览器，该方法将不会关闭传入的浏览器，返回 browser
    # 若使用外部浏览器  # 注意在外部关闭浏览器
    # 若要使用不同随机UA头，随机IP 请求网页的话建议使用方法的内部浏览器（只传入 url）
    # 若要使用同一个UA头，同一个IP 请求网页的话建议使用外部浏览器（传入 url 和 browser）
    # 在外部创建浏览器时，可以使用 selenium_init 方法
    try:
        if not browser:  # 创建浏览器
            use_def_browser = True  # 更改旗标
            browser = selenium_init()  # 可在 selenium_init 方法中写 获取随机UA头，代理IP

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


if __name__ == '__main__':
    # browser = selenium_init()

    url = 'https://news.sina.com.cn/roll/'
    # html_str = requests_get_url(url)  # requests
    html_str = selenium_get_url(url)  # selenium 使用内部浏览器
    # html_str = selenium_get_url(url, browser)  # selenium 使用外部浏览器
    # browser.quit()
    print(html_str)

