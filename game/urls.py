from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('game', views.game),
    path('leaderboard', views.leaderboard)
]
