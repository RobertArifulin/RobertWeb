from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/home.html')


def sing_up(request):
    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def password_recovery(request):
    return render(request, 'accounts/passrecover.html')

