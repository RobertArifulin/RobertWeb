from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home page')


def game(request):
    return HttpResponse('Game page')

def leaderboard(request):
    return HttpResponse('Leaderboard page')
