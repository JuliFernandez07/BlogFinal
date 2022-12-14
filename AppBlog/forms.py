from django import forms
from ckeditor.widgets import CKEditorWidget

class cargar_receta(forms.Form):
    nombre_receta = forms.CharField(max_length=100, required=True)
    descripcion_receta = forms.CharField(max_length=240, required=True)
    # receta = forms.CharField(max_length=5000, widget=forms.Textarea, required=True)
    receta = forms.CharField(max_length=5000, widget=CKEditorWidget(), required=True)
    imagen = forms.ImageField(required=False)
