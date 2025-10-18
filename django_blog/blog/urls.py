from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts-list'),
    path('posts/new/', PostCreateView.as_view(), name='posts-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='posts-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='posts-delete'),
]

