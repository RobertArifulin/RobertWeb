from django.shortcuts import render
from django.http import HttpResponse


def game(request):
    return render(request, 'game/game.html')


def leaderboard(request):
    return render(request, 'game/leaderboard.html')
