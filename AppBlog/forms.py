from django import forms
from AppBlog.models import receta 

class cargar_receta(forms.Form):
    nombre_receta = forms.CharField(max_length= 100)
    descripcion_receta = forms.CharField(max_length= 240)
    receta = forms.CharField(max_length= 5000)
    imagen = forms.ImageField(required=False)
    