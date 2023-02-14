from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

# 引入models文件
from App import models
from App.models import UserInfo

# 现在这些方法其实是前端完成的


# Create your views here.
# 【1】注意这里的request 是默认要这样写的
def index(request):
    # 简单使用HttpR方法返回字符串
    # return HttpResponse("欢迎使用")

    # 但是如果想要返回网页就要用
    return render(request, 'index.html')


# 【2】浏览器向网页的请求
def something(request):
    # request 其实是一个对象，
    # 封装了用户通过浏览器发送过来的所有（请求相关）的数据

    # 1.请求获取方式 GET/POST 我们用哪种，method就是哪种
    print(request.method)

    # 2.url上传递值
    print(request.GET)

    # 3.将发送的数据通过请求体提交数据
    print(request.POST)

    # 4.【响应】HttpResponse("返回内容")，内容字符串返回给请求者
    # return HttpResponse("返回网页的内容")

    # 5.【响应】读取HTML的内容+渲染（替换）-> 生成新的字符串
    # return render(request, 'something.html', {"title": "消息已发送"})

    # 6.【响应】网页重定向
    return redirect("https://www.baidu.com")


# 【3】用户简单登录
def login(request):
    # 根据请求的方式不同，当请求为get时直接显示页面
    if request.method == "GET":
        return render(request, "login.html")

    # 打印信息
    print(request.POST)

    # 如果是post请求，获取用户提交的数据
    username = request.POST.get("user")
    password = request.POST.get("pwd")

    if username == 'root' and password == "123":
        return HttpResponse("登录成功")
        # return redirect("https://www.baidu.com")

    # 用户输入错误，登录失败
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})

    # else:
    #     # 获取用户提交的数据
    #     print(request.POST)
    #     return HttpResponse("登录成功！")


# 【4】测试orm操作表中的数据
def orm(request):
    # Department.objects.create(title="诊疗部")
    # Department.objects.create(title="标记免疫检测部")
    # Department.objects.all().delete()

    # UserInfo.objects.create(name="王孟", password="123", age=22)
    # UserInfo.objects.create(name="张帅", password="1234", age=22)
    # UserInfo.objects.create(name="王浩翔", password="12345", age=22)

    # 查询数据
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    # 更新数据
    # UserInfo.objects.all().update(password=999)
    # UserInfo.objects.filter(id=2).update(age=999)
    # UserInfo.objects.filter(name="王孟").update(age=999)
    return HttpResponse("成功")


# 【5】用户管理
def user_manage(request):
    # 获取数据库中的所有的用户信息
    # 其实就是存储着一行行的对象的列表
    data_list = UserInfo.objects.all()
    # print(data_list)

    return render(request, "user_manage.html", {"data_list": data_list})


# 【6】用户添加
def user_add(request):
    # 如果是GET请求，则返回
    if request.method == "GET":
        return render(request, "user_add.html")
    # 获取用户提交的数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    # 添加到数据库
    UserInfo.objects.create(name=user, password=pwd, age=age)
    # return HttpResponse("用户添加成功")

    # 但是实际上，我们添加完用户之后应该立即跳转到我们的user_manage
    return redirect("/user_manage/")


# 【7】用户删除
def user_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user_manage/")


# 【8】用户登录 携带token
def adminLogin(request):
    # username = request.POST.get("user")
    # password = request.POST.get("pwd")
    # 简单写一个返回结果
    res = {
        'code': 0,
        'msg': '登录成功'
    }

    # request.POS获取请求格式为POST
    if request.POST:
        # request.POST.get获取POST请求参数
        username = request.POST.get('username')  # 用户名
        password = request.POST.get('password')  # 密码
        # 登陆 查询数据库的所有字段，查询的数据结果是一个数组包含字典 <QuerySet [{'id': 1, 'username': 'admin', 'password': 'admin'}, {'id': 2,
        # 'username': 'zzx', 'password': 'zzx'}]>
        Login = models.Login.objects.values()
        data_list = UserInfo.objects.all()
        # 遍历数据库数据
        for i in data_list:
            if i['username'] == username and i['password'] == password:
                # JsonResponse(res)返回json格式
                 return JsonResponse(res)

        res['code'] = 1
        res['msg'] = "账号密码不正确"
        return JsonResponse(res)

