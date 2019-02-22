from django.urls import path
from django.contrib import admin

# from icProject.icApp import views
from . import views

urlpatterns = [
    path('home/<name>/', views.index, name='index'),
    path('home/details/<name>/', views.details, name='details'),
]