from django.contrib import admin
from django.urls import path
from . import views



app_name = "app"

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),

]