from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('ip/', views.iplist, name = 'iplist' ),
    path('assign/', views.assign, name = 'assign'),
    path('subnets/', views.subnets, name ='subnets'),
    path('js/', views.jstest, name = 'jstest'),
]