# djangotest\apps\users\views.py 下

class PageNotFoundAndPageError:

    def page_not_found(self, request):
        response = render_to_response('404.html', {})
        response.status_code = 404
        return response

    def page_error(self, request):
        response = render_to_response('500.html', {})
        response.status_code = 500
        return response



#




# 在 djangotest\djangotest\settings.py 中配置

DEBUG = True   # 默认 True 生产环境 打印所以错误信息，False进入部署环境（False启用 404 500全局）

ALLOWED_HOSTS = ['*']

handler404 = 'users.views.PageNotFoundAndPageError.page_not_found'
handler500 = 'users.views.PageNotFoundAndPageError.page_error'
