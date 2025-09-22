from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import View

User = get_user_model()

COLUMNS = [
    "first_name",
    "last_name",
    "username",
    "email",
    "is_staff",
    "is_active",
    "is_superuser",
    "last_login",
    "date_joined",
]

class UserReportView(View):

    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=users.csv"