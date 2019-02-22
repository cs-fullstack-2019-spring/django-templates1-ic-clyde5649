from django.urls import path
from django.contrib import admin

# from icProject.icApp import views
from . import views

urlpatterns = [
    path('home/<name>/', views.index, name='index'),
]