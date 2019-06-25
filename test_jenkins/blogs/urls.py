# _*_coding:utf-8_*_
# 创建用户  ：chenzhengwei
# 创建日期  ：2019/6/25 下午1:02

from blogs.views import BlogsIndex
from django.conf.urls import url


urlpatterns = [
    url('^index/$',BlogsIndex.as_view())
]