"""book_shop URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from book import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^reg/$", views.register),
    url(r'^index/$', views.index),
    url(r'^check_username_exist/', views.check_username_exist),
    url(r"^error/$", views.error),
    url(r'^login/', views.login),
    url(r'^get_valid_img.png/', views.get_valid_img),
    url(r'^logout/',views.logout),
    url(r"^activate/(\d+)",views.activate),
    url(r"^baoming/(\d+)",views.baoming),
    url(r"^remen/",views.remen),
    url(r"^huojiang/",views.huojiang),
    url(r"^find_book/$",views.find_book),
    url(r"^find/(\d+)",views.find),
    url(r"^add_comment/$",views.add_comment),
    url(r"^shoucang/(\d+)",views.shoucang),
    url(r"^dianzan/(\d+)/(\d+)",views.dianzan),
    url(r"^home/$",views.home),
    url(r"^score/$",views.score),
]
