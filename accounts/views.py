from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views import View
from .forms import RegistrationForm


class RegisterView(View):
    def get(self, request):
        form= RegistrationForm()
        return render(request, "registration/register.html", {"form": form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("home")

           # return redirect("accounts:login")
        return render(request, "registration/register.html", {"form": form})