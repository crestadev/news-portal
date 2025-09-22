from django.urls import include, path

from report import views

app_name = "report"

urlpatterns = [
    path("users/", views.UserReportView.as_view(), name="users"),
]