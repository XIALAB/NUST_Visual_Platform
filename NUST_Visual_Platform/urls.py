"""NUST_Visual_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views
urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^njustmark/', include('njustmark.urls', namespace="njustmark")),
    url(r'^wangyi/', include('wangyi.urls', namespace="wangyi")),
    url(r'^music/', include('music.urls', namespace="music")),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG404:
    urlpatterns += patterns('',
            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': os.path.join(os.path.dirname(__file__), '../static')} ),
            )
