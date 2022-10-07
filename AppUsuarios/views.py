import email
from django.shortcuts import render
from AppUsuarios.forms import *
from AppUsuarios.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            registerOK = True
            contexto = {"mensaje": "Usuario Creado :)", "registerOK": registerOK}

    else:
        #form = UserCreationForm()       
        form = RegisterForm()
        registerOK = False
        contexto = {"form": form, "registerOK": registerOK }

    return render(request, "register.html", contexto)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                loginOK = True
                contexto = {"mensaje": f"Bienvenido {usuario}.", "loginOK": loginOK, "user": user.username}

                return render(request,"login.html", contexto)

            else:
                loginOK = False
                contexto = {"mensaje": "Error, formulario erroneo.", "loginOK": loginOK}

                return render(request,"login.html", contexto)

        else:
            loginOK = False
            form = AuthenticationForm()
            contexto = {"mensaje": "Error, verifique usuario y/o contraseña.", "loginOK": loginOK, "form": form}
            
            return render(request,"login.html" , contexto)

    form = AuthenticationForm()
    loginOK = False

    contexto = {"form": form, "loginOK": loginOK}

    return render(request,"login.html" , contexto)

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Saliste sin problemas")

    return redirect("inicio")

@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        mi_formulario = edicionUsuarioForm(request.POST)

        if mi_formulario.is_valid:
            print(mi_formulario)

            info = mi_formulario.cleaned_data

            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
           
            

            usuario.save()

            return render(request, "Inicio.html")


    else:
        mi_formulario = edicionUsuarioForm(initial = {"email" : usuario.email})

        return render (request, "editarPerfil.html", {"miFormulario": mi_formulario, "usuario": usuario})