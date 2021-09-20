from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup', views.sing_up),
    path('login', views.login),
    path('pass_recovery', views.password_recovery),
]
