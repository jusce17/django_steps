from django.urls import re_path
from firstApp import views

urlpatterns = [

     re_path(r'^$', views.index, name = 'index'),
]
