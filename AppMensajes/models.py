from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mensajes(models.Model):
    fecha = models.DateTimeField()
    emisor = models.CharField(max_length = 100)
    receptor = models.CharField(max_length = 100)
    cuerpo = models.CharField(max_length = 5000)
    leido = models.BooleanField()
