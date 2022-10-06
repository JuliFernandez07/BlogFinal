from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 240)
    email = models.EmailField()
