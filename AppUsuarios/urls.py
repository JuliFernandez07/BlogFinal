from django.contrib import admin
from django.urls import path
from AppUsuarios.views import *

urlpatterns = [
    path("register/", register, name="Register"),
    path("login/", login, name="Login"),
    path("logout/", logout, name="Logout"),
]