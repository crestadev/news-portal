from django.urls import include, path

from report import views


urlpatterns = [
    path("users/", views.UserReportView.as_view(), name="users"),
]