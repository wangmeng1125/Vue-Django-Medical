from django.db import models


# 用户数据
# ===========================================================================
#  =============================【用户数据】===================================
# ===========================================================================
# Create your models here.
# 我们写了一个类 然后定义我们的变量 和最常的长度
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


# ===========================================================================
#  =============================【算法数据】===================================
# ===========================================================================
# 算法数据
class AlgorithmInfo(models.Model):
    algorithm_name = models.CharField(max_length=32)
    type = models.CharField(max_length=64)


# 模型数据
class ModelInfo(models.Model):
    model_name = models.CharField(max_length=32)
    type = models.CharField(max_length=64)

# 管理员表
# class Admin_Info(models.Model):
#     name = models.CharField(max_length=64)  # 管理员姓名
#     password = models.CharField(max_length=64)  # 管理员登录密码

# 当我们创建了这个类之后，会自动在数据库中生成一个表
# 这个表的名称为 App_userinfo

# 部门表
# class Department(models.Model):
#     title = models.CharField(max_length=16)

# 在Department（部门）表中新建机构
# 核医学的两个主要部门
# Department.objects.create(title="诊疗部")
# Department.objects.create(title="标记免疫检测部")
#
# UserInfo.objects.create(name="王孟", password="123", age=22)
# UserInfo.objects.create(name="张帅", password="1234", age=22)
# UserInfo.objects.create(name="王浩翔", password="12345", age=22)
# class Login:
#     objects = None
