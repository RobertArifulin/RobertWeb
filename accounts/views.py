from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home page')


def sing_up(request):
    return HttpResponse('Sing up page')


def login(request):
    return HttpResponse('Login page')


def password_recovery(request):
    return HttpResponse('Password recovery page')

