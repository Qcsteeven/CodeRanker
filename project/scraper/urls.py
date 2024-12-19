from django.urls import path
from . import views
from django.shortcuts import render



urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_list, name='books_list'),
    path('languages/', views.languages_list, name='languages_list'),
]
