"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import get_verify_img
from . import draw
urlpatterns = [
    url(r'^check/$', get_verify_img.get_verify_img),
    url(r'^draw/$',draw.drawpicture),
    
]#路径为根目录正则表达式，执行hello函数
#path('hello',view.hello),path(route,view,kwargs = None(视图使用的字典类型参数), name = None(反向获取url))