from django.contrib import admin
from django.urls import path
from . import views

from AppBlog.views import fulano

urlpatterns = [
    
    path("", views.fulano),
    path("cargarReceta/", views.cargarReceta),
    path("verReceta/", views.verReceta),
]
    