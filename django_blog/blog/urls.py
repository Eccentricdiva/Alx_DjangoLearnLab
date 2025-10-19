from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Post CRUD routes
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_update, name='post_update'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),

    # New features
    path('search/', views.search_posts, name='search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
]
