from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Post URLs
    path('posts/', PostListView.as_view(), name='posts-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_pk>/comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
