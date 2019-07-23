from django.contrib import admin
from django.urls import path, re_path
from . import views

# namespace
app_name = 'js'

urlpatterns = [
    #path('', views.index, name = 'home'),
    #path('aj/', views.load_cities, name ='ld'),
    #path('add/'), views.personcreate, name = 'add'),
    # 创建新客户
    re_path(r'^client/create/$', views.ClientCreateView.as_view(), name='client_create'),

    # 显示客户详情
    re_path(r'^client/(?P<pk>\d+)/$', views.ClientDetailView.as_view(), name='client_detail'),

    # Ajax调用城市清单
    re_path(r'^ajax/load_cities/$', views.ajax_load_cities, name='ajax_load_cities'),

       

]