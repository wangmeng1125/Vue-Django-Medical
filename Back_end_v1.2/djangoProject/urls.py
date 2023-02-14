from django.urls import path
# from App import admin
# from App import admin
from App.api import api

urlpatterns = [
    # 【1】默认主页的地址
    # path('index/', views.index),

    # 【2】请求和响应
    # path('something/', views.something),

    # 【3】测试对数据库的增删改查
    # path('orm/', views.orm),

    # 【4】用户登录
    # path('login/', views.login),

    # 【5】用户管理
    # path('user_manage/', views.user_manage),

    # 【6】添加用户
    # path('user_add/', views.user_add),

    # 删除用户
    # path('user_delete/', views.user_delete),

    # path('admin/', admin.site.urls),

    # 后端解口 API 路由
    path('api/', api.urls)


]
