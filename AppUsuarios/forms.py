from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
    
class edicionUsuarioForm(forms.Form):
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 
        help_texts = {k:"" for k in fields}


class formularioAvatar(forms.Form):
    imagen = forms.ImageField(required=True)

    # class Meta:
    #     model = User
    #     fields = ['imagen'] 
    #     help_texts = {k:"" for k in fields}
