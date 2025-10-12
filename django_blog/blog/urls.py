from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # home page of blog
]
from django.shortcuts import render, get_object_or_404
from .models import Post

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
