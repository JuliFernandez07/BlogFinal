from django.contrib import admin
from django.urls import path
from AppUsuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accounts/signup/", signup, name="signup"),
    path("accounts/login/", login_request, name="Login"),
    path("accounts/logout/", LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path("accounts/profile/", editar_usuario, name= "EditarUsuario"),
    path("accounts/profile_password/", editar_password, name= "EditarPassword"),
    path("accounts/avatar/", editar_avatar, name= "EditarAvatar"),
]