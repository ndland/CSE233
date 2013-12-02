from django.conf.urls import patterns, include, url

# from django.contrib import admin
from converter import views

urlpatterns = patterns('',
    url('^$', views.mainview, name='index'),
    url('^doconversion$', views.doconvert, name='doconvert'),
)
