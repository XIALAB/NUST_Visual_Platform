#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^([0-9]{2})$', views.show_1, name='show_1'),
        url(r'^(?P<year>[0-9]{4})', views.show_2, name='show_2'),
        ]
