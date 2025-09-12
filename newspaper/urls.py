from django.urls import path
from newspaper import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
]