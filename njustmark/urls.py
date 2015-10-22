from django.conf.urls import include, url

from . import views
from .views import NewUploadView

urlpatterns = [
    url(r'^$','njustmark.views.index'),
    url(r'^upload/temp','njustmark.views.download'),
    url(r'^upload/','njustmark.views.upload'),
    url(r'^nexttext/','njustmark.views.nexttext'),
    url(r'^ReExce/','njustmark.views.ReExce'),
    url(r'^save/','njustmark.views.save'),
    url(r'^back/','njustmark.views.back'),
    # url(r'^newupload/', views.newupload, name='newupload'),
    url(r'^newupload/', NewUploadView.as_view(), name='newupload'),
]
