from django.contrib import admin
from django.urls import path
from . import views
from AppBlog.views import *

urlpatterns = [
    path("", inicio, name="Home"),
    path("cargarReceta/", cargarReceta, name="cargarReceta"),
    path("verReceta/<receta_id>", verReceta, name="verReceta"),
]
