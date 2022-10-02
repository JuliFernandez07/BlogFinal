from django import forms

from AppBlog.models import receta 



class cargar_receta(forms.Form):
    nombre_receta = forms.CharField(max_length= 100)
    imagen = forms.ImageField(required=False)
    receta = forms.CharField(max_length= 5000)
    