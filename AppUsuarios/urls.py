from django.contrib import admin
from django.urls import path
from AppUsuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", register, name="Register"),
    path("login/", login_request, name="Login"),
    path("logout/", LogoutView.as_view(template_name='logout.html'), name="Logout"),
]