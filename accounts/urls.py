from django import views
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.forms import LoginForm

app_name = "accounts"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(authentication_form=LoginForm),name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
]
