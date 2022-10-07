from django.contrib import admin

from AppBlog.models import receta
from AppUsuarios.models import avatar, usuario
from .models import *

# Register your models here.
admin.site.register(receta)

admin.site.register(avatar)

