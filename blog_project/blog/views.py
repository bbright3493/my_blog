# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.conf import  settings
# Create your views here.


def global_setting(request):
    # 站点基本信息
    SITE_URL = settings.SITE_URL
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC

    # 广告数据（同学们自己完成）
    # 标签云数据（同学们自己完成）
    # 友情链接数据（同学们自己完成）
    # 文章排行榜数据（按浏览量和站长推荐的功能同学们自己完成）
    return locals()


def index(request):
    return render(request, 'index.html')