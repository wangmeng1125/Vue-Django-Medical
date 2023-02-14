# 该文件是用来写所有的后端接口的
from typing import List

# from django.http import JsonResponse, HttpResponse
from ninja import NinjaAPI
from django.contrib import auth
from django.contrib.auth.models import User
# 加密和校验的方法
from django.contrib.auth.hashers import make_password, check_password
# from App import models
# from sqlalchemy.sql.functions import user

from App.models import UserInfo
from App.scheme import UserSchema, NotFoundSchema, AdminSchema,ModelSchema,AlgoritmSchema

# Admin_Info

api = NinjaAPI()


# ===========================================================================
#  =============================【用户接口】===================================
# ===========================================================================
# 【1】用户登录
@api.post("/App/login/")
def admin_login(request, payload: AdminSchema):
    user = auth.authenticate(username=payload.username, password=payload.password)
    print(user)
    print("登录成功")
    if user is not None:
        return {"code": "200", "success": True, "msg": "login success", "token": "我是管理员"}
    else:
        return {"success": False, "msg": "login fail"}


# 【2】查询用户信息
# 查询所有的用户
@api.get("/App/user_info", response=List[UserSchema])
def User(request):
    data = UserInfo.objects.all().values()
    print(data)
    # data[{"key": "value"}] = user
    # user.data()
    # return UserInfo.objects.all() # 查询所有的用户
    return data


# 【3】根据ID查询用户
@api.get("/App/user_info/{user_id}", response={200: List[UserSchema], 404: NotFoundSchema})
def User(request, user_id: int):  # 这个路径拼接后面多一个user_id
    try:  # 同时对这个id 进行约束必须为整形
        user = UserInfo.objects.get(pk=user_id)
        # print(user)                    # 调试用的，不看的话可以不要
        return [user]
    except UserInfo.DoesNotExist as e:
        return 404, {"message": "该用户不存在"}


# 【4】添加用户
@api.post("/App", response={201: UserSchema})
def create_user(request, user: UserSchema):
    UserInfo.objects.create(**user.dict())
    return user


# 【5】修改用户信息
@api.put("/App/update/{user_id}", response={200: UserSchema, 404: NotFoundSchema})
def edit_userInfo(request, user_id: int, data: UserSchema):
    try:
        user = UserInfo.objects.get(pk=user_id)  # 通过主键的方式获取到用户
        for attribute, value in data.dict().items():
            setattr(user, attribute, value)
        user.save()
        return 200, user
    except UserInfo.DoesNotExist as e:
        return 404, {"message": "该用户不存在！"}


# 【6】删除用户信息
@api.delete("/App/{user_id}", response={200: None, 404: NotFoundSchema})
def delete_userInfo(request, user_id: int):
    try:
        user = UserInfo.objects.get(pk=user_id)  # 通过主键的方式获取到用户
        user.delete()  # 删除用户信息
        return 200
    except UserInfo.DoesNotExist as e:
        return 404, {"message": "该用户不存在！"}


# ===========================================================================
#  =============================【算法接口】===================================
# ===========================================================================
# 【7】模型创建上传接口
@api.post("/App/algorithm_upload", response={201: ModelSchema})
def create_user(request, user: UserSchema):
    UserInfo.objects.create(**user.dict())
    return user


# 【8】模型训练测试接口
@api.post("/App/model_training", response={201: AlgoritmSchema})
def create_user(request, user: AlgoritmSchema):
    UserInfo.objects.create(**user.dict())
    return user


# 【9】算法展示接口
@api.post("/App/algorithm_show", response={201: AlgoritmSchema})
def create_user(request, user: AlgoritmSchema):
    UserInfo.objects.create(**user.dict())
    return user
