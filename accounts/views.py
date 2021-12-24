from django.shortcuts import render
from django.http import HttpResponse
from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as djlogin
from . import models


def home(request):
    return render(request, 'accounts/home.html')


def logged_out(request):
    return render(request, 'accounts/logged_out.html')


# @unauth_user
def sing_up(request):
    form = models.CreateUserForm(request.POST)
    # form._meta.get_field('email')._unique = True
    if form.is_valid():
        user = form.save()
        return render(request, 'accounts/login.html')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    message = 'Успех'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            djlogin(request, user)
            return render(request, 'accounts/home.html')
        else:
            message = "Неверный логин или пароль"
    context = {'message': message}
    return render(request, 'accounts/login.html', context)


def password_recovery(request):
    return render(request, 'accounts/password_reset_form.html')
