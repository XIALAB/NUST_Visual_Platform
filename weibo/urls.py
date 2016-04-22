#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.show, name='weibo'),
        url(r'^noob/$', views.test, name='test'),
        # url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
        ]
