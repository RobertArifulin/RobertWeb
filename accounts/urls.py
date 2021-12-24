from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.sing_up),
    path('login', views.login),
    path('accounts/logout/', views.password_recovery),
    path('accounts/logout/', views.logged_out),
]
