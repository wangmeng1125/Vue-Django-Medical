"""
WSGI config for djangoProject project.
它将 WSGI 可调用对象公开为名为“应用程序”的模块级变量。
有关此文件的详细信息，请参阅
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/


但是Django3 的异步请求还是不成熟现在多数用的还是同步请求
也就是 asgi 和 wsgi 这两个是用来接收来自网络的请求的，
然后将请求传递给我们的Python函数


"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

application = get_wsgi_application()
