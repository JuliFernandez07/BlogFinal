from django.contrib import admin
from django.urls import path
from AppMensajes.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("messages/", messages, name="Mensajes"),
    path("messages/chat/<receptor>", chat, name="Chat"),

]

