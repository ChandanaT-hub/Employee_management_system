
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('view_book', views.view_book, name='view_book'),
    path('add_book', views.add_book,name='add_book'),
    path('remove_book', views.remove_book, name='remove_book'),
    path('filter_book', views.filter_book, name='filter_book'),
]

