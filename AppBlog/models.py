from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

class receta(models.Model):
    fecha = models.DateField()
    nombre_receta = models.CharField(max_length=100)
    descripcion_receta = models.CharField(max_length=240)
    receta = models.CharField(max_length=5000)
    autor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="Recetas/", null=True, blank=True)
    #autor = models.ForeignKey(User, on_delete=models.CASCADE)
