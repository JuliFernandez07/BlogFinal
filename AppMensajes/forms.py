from django import forms

class enviar_mensaje(forms.Form):
    receptor = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    cuerpo = forms.CharField(max_length=5000, required=True, widget=forms.Textarea, label="Mensaje")

class volver_opciones_mensaje(forms.Form):
    receptor = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())