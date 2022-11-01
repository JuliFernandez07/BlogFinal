from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField

class receta(models.Model):
    fecha = models.DateField()
    nombre_receta = models.CharField(max_length=100)
    descripcion_receta = models.CharField(max_length=240)
    receta = RichTextField()
    # autor = models.CharField(max_length=100, default='')
    autor_usuario = models.CharField(max_length=100, default='')
    autor_nombre = models.CharField(max_length=100, default='')
    imagen = models.ImageField(upload_to="Recetas/", null=True, blank=True)
    #autor = models.ForeignKey(User, on_delete=models.CASCADE)
