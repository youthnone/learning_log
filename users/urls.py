"""为应用程序users定义URL模式"""

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # 登录页面
    path(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    path(r'^logout/$',views.logout_view,name = 'logout' ),
    path(r'^register/$',views.register,name='register')

]
