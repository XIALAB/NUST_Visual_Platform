from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$','njustmark.views.index'),
    url(r'^upload/temp','njustmark.views.download'),
    url(r'^upload/','njustmark.views.upload'),
    url(r'^nexttext/','njustmark.views.nexttext'),
    url(r'^ReExce/','njustmark.views.ReExce'),
    url(r'^save/','njustmark.views.save'),
    url(r'^back/','njustmark.views.back'),
)
