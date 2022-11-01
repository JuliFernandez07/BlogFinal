from django.contrib import admin
from django.urls import path
from AppBlog.views import *

urlpatterns = [
    path("", inicio, name="Home"),
    path("cargarReceta/", cargarReceta, name="cargarReceta"),
    path("verReceta/<receta_id>", verReceta, name="verReceta"),
    path("editarReceta/<receta_id>", editarReceta, name="editarReceta"),
    path("editadaReceta/", editadaReceta, name="editadaReceta"),
    path("about/", about, name="About")
]
