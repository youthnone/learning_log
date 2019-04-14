"""为应用程序users定义URL模式"""

from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views
from django.conf.urls import url

urlpatterns = [
    # 登录页面
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    # 注销
    # url(r'^logout/$',views.logout_view,name='logout'),
    #这两种方法都可行
    path('logout/',views.logout_view,name='logout'),
]
