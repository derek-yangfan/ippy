from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('admin/', views.index, name = 'home'),
    path('IP/', views.iplist, name = 'ip_entry'),    
    path('subnets/', views.subnets, name = 'subnets.html'),
    path('request/', views.ip_request, name = 'ip_request.html'),
    re_path(r'^subnets/$', views.subnets, name = 'subnets'),
    path('assign/', views.assign, name = 'assign.html'),
    re_path('^assign/$', views.assign, name = 'assign'),
    re_path(r'^map/$',views.Map),
    re_path(r'^GetCityData/$',views.Return_City_Data),
    re_path(r'^GetCountryData/$',views.Return_Country_Data),
    path('load/', views.load_site),

]