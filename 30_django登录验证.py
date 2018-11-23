# 在 djangotest\utils\mixin_utils.py 下重载

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)




#




# 在 djangotest\apps\data\views.py 下使用 LoginRequiredMixin

from utils.mixin_utils import LoginRequiredMixin


class TestView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "test.html")
