from django.urls import path
from .views import (
    post_list, post_detail, post_create, post_update, post_delete,
    search_posts, PostByTagListView
)

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<slug:slug>/edit/', post_update, name='post_update'),
    path('post/<slug:slug>/delete/', post_delete, name='post_delete'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
