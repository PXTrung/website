from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from .models import Profile


def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username, email, password)

        user.save()

        profile = Profile()
        profile.phone = request.POST["phone"]
        profile.address = request.POST["address"]
        profile.user = user

        profile.save()

        return redirect('product')

    context = {"form": form}
    return render(request, "customer/register.html", context)
  