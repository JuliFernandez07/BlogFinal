from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 240)
    email = models.EmailField()

class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to = "avatares", null = True, blank = True)
