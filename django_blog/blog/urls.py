from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Blog URLs
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),

    # Authentication URLs
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),  # ✅ our custom logout
    path("profile/", views.profile, name="profile"),
]
