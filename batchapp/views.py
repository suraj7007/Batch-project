from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.decorators import api_view


def loginuser(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user_auth = authenticate(username=uname, password=pwd)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('home')
        else:
            messages.error(
                request, 'Entered username or password is incorrect')
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect('login')


def signupuser(request):
    if request.method == "POST":
        uname = request.POST.get("id_username")
        pass1 = request.POST.get("id_password1")
        pass2 = request.POST.get("id_password2")
        if User.objects.filter(username__iexact=uname).exists():
            messages.error(
                request, "This  Username is  already exist please try another email")
            return redirect('signup')
        else:
            if pass1 == pass2:
                User.objects.create_user(
                    username=uname, password=pass1)
                messages.success(
                    request, 'Congratulations you have registered successfully')
                return redirect('login')
            else:
                messages.error(
                    request, "The password confirmation does not match with password.")
                return redirect('signup')
    return render(request, "signup.html")


@api_view(["GET"])
@login_required(login_url="login")
def home(request):
    batch_obj = Batch.objects.filter(user=request.user)
    serializer = BatchSerializers(batch_obj, many=True)
    context = {"data":serializer.data}
    return render(request, "home.html", context)
