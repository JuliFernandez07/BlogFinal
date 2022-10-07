from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField


class usuarioFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput) 
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

    
class edicionUsuarioForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class formularioAvatar(forms.Form):
    imagen = forms.ImageField(required=True)