from django.contrib import admin
from django.urls import path
from . import views

from AppBlog.views import *

urlpatterns = [
    
    path("", views.fulano),
    path("Home/", inicio, name="Home"),
    path("cargarReceta/", cargarReceta, name="cargarReceta"),
    path("verReceta/", verReceta, name="verReceta"),
]
    