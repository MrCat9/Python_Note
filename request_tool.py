# -*- coding: utf-8 -*-


from selenium import webdriver
import requests
from retrying import retry
import re
import eventlet
import time
from datetime import datetime
import random
import w3lib.html

from settings import CHROMEDRIVER_EXECUTABLE_PATH, SELENIUM_IMPLICITLY_WAIT
from settings import REQUESTS_TIMEOUT, RETRY_TIMES


# # selenium
# CHROMEDRIVER_EXECUTABLE_PATH = 'F:/chromedriver_win32/chromedriver.exe'
# FIREFOXDRIVER_EXECUTABLE_PATH = 'F:/geckodriver-v0.24.0-win64/geckodriver.exe'
# SELENIUM_IMPLICITLY_WAIT = 10
#
# # requests
# REQUESTS_TIMEOUT = 10

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
    "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"
]


def requests_init():
    params = {}

    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'User-Agent': random.choice(ua_list),
        # 'User-Agent': get_ua(),  # 获取随机 UA头
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


def retry_if_timeout(exception):
    if isinstance(exception, requests.exceptions.ConnectTimeout):
        print('requests.exceptions.ConnectTimeout')
        return True
    if isinstance(exception, requests.exceptions.ReadTimeout):
        print('requests.exceptions.ReadTimeout')
        return True
    return False


# timeout的话重试5次
@retry(stop_max_attempt_number=RETRY_TIMES, retry_on_exception=retry_if_timeout, wait_random_min=1, wait_random_max=5)
def requests_get_url(url):
    # ================================ 生成 requests 的 get 方法的参数 ================================
    params, headers, proxies, timeout = requests_init()  # 可在 requests_init 方法中写 获取随机UA头，代理IP
    # =================================================================================================

    # ================================ 请求网页 ================================
    # response = requests.get(url=url, params=params, headers=headers, proxies=proxies, timeout=timeout)
    # html_str = response.text
    eventlet.monkey_patch()
    try:
        with eventlet.Timeout(timeout * 2):  # 限制网页请求和源码计算的总时长
            response = requests.get(url=url, params=params, headers=headers, proxies=proxies, timeout=timeout)
            html_str = response.text
    except:
        print('[eventlet.Timeout][request_tool][', datetime.now(), '][msg:][url:', url, ']')
    if not response or not html_str:
        raise Exception('eventlet.Timeout')
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
    # user_agent = None
    user_agent = random.choice(ua_list)

    # 获取随机 代理IP
    # ip, port = ('114.55.236.62', '3128')
    ip, port = (None, None)

    # ================================ 浏览器 ================================
    # 设置浏览器
    chrome_options = webdriver.ChromeOptions()

    # 设置无界面浏览
    # chrome_options.set_headless(True)
    chrome_options.add_argument('--headless')    

    # 设置 user_agent
    if user_agent:
        chrome_options.add_argument('user-agent={}'.format(user_agent))

    # 设置代理 IP
    if ip and port:
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
        time.sleep(3)  # 等待网页加载  # 考虑用url数量动态判断等待时长

        # # 切换到新打开的页面
        # current_window = browser.current_window_handle
        # all_handles = browser.window_handles
        # for handle in all_handles:
        #     if handle != current_window:
        #         browser.switch_to.window(handle)
        
        # # 切换到 iframe 下
        # browser.switch_to.frame('iframe_id')
        
        html_str = browser.page_source

        if not use_def_browser:
            return html_str, browser
        else:
            return html_str
    except Exception as e:
        print('[error][request_tool][', datetime.now(), '][msg:', str(e), '][url:', url, ']')
    finally:
        if browser and use_def_browser:
            browser.quit()


def html_str_noise_reduce(html_str):
    # re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    # html_str = re_comment.sub('', html_str)  # 去除HTML注释  # 去除单行的注释，且注释中的内容不含>

    # re_script = re.compile('<s*script[^>]*>[^<]*<s*/s*scripts*>', re.I)  # 去除 script 标签及其内容
    # html_str = re_script.sub('', html_str)

    # re_style = re.compile('<s*style[^>]*>[^<]*<s*/s*styles*>', re.I)  # style
    # html_str = re_style.sub('', html_str)  # 去除 style

    html_str = w3lib.html.remove_comments(html_str)  # 去除注释
    html_str = w3lib.html.remove_tags_with_content(html_str, which_ones=('style',))  # 去除 style 标签及其内容

    return html_str


if __name__ == '__main__':
    # browser = selenium_init()

    url = 'https://news.sina.com.cn/roll/'
    # html_str = requests_get_url(url)  # requests
    html_str = selenium_get_url(url)  # selenium 使用内部浏览器
    # html_str = selenium_get_url(url, browser)  # selenium 使用外部浏览器
    # browser.quit()
    html_str = html_str_noise_reduce(html_str)
    print(html_str)

