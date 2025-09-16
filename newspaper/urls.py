from django.urls import path
from newspaper import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("post-list/", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactCreateView.as_view(), name="contact"),
    path("tag-list/", views.TagListView.as_view(), name="tag-list"),
    path("category-list/", views.CategoryListView.as_view(), name="category-list"),
    path("post-by-category/<int:category_id>/", views.PostByCategoryView.as_view(), name="post-by-category"),
    path("post-by-tag/<int:tag_id>/", views.PostByTagView.as_view(), name="post-by-tag"),

]
