import email
from django.shortcuts import render, redirect
from AppUsuarios.forms import *
from AppUsuarios.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        print(form)
        
        if form.is_valid():
            print("Ingrese al primer form.is_valid")
            # username = form.cleaned_data['username']
            form.save()
            registerOK = True
            contexto = {"mensaje": "Usuario Creado :)", "registerOK": registerOK}
        else:
            print("Ingrese al ELSE del IF form.is_valid")
            form = RegisterForm()
            registerOK = False
            contexto = {"mensaje": "Error en el formulario", "registerOK": registerOK}

    else:
        #form = UserCreationForm()       
        form = RegisterForm()
        registerOK = False
        contexto = {"form": form, "registerOK": registerOK }

    return render(request, "signup.html", contexto)



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

                return redirect("Home")

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

    return redirect("Home")


@login_required
def editar_usuario(request):

    usuario = request.user
    imagen_avatar = list(avatar.objects.filter(user=request.user.id))

    if imagen_avatar != []:
        imagen_avatar = imagen_avatar[0].imagen.url
    else:
        imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

    if request.method == "POST":

        mi_formulario = edicionUsuarioForm(request.POST, request.FILES)

        if mi_formulario.is_valid():

            info = mi_formulario.cleaned_data
            
            print(info)

            usuario.username = info["username"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.email = info["email"]
            usuario.save()

            editPerfil = True

        else:
            editPerfil = False
            # return render(request, "Inicio.html")


    else:
        initialValues = {
                            "username": usuario.username,
                            "first_name": usuario.first_name,
                            "last_name": usuario.last_name,
                            "email" : usuario.email
                        }

        mi_formulario = edicionUsuarioForm(initial = initialValues)
        editPerfil = False

    return render(request, "editarPerfil.html", {"miFormulario": mi_formulario, "usuario": usuario, "editPerfil": editPerfil, "imagen": imagen_avatar})




@login_required
def editar_avatar(request):

    imagen_avatar = list(avatar.objects.filter(user=request.user.id))

    if imagen_avatar and imagen_avatar != []:
        imagen_avatar = imagen_avatar[0].imagen.url
    else:
        imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

    usuario = request.user

    try:
        change_avatar = avatar.objects.get(user=request.user.id)
        change_avatar.delete()

    finally:

        if request.method == "POST":

            mi_formulario = formularioAvatar(request.POST, request.FILES)

            if mi_formulario.is_valid():
                u = User.objects.get(id=request.user.id)
                info = mi_formulario.cleaned_data
                nuevo_avatar = avatar(user=u, imagen=info['imagen']) 
                nuevo_avatar.save()

                editAvatar = True

            else:
                editAvatar = False
                # return render(request, "Inicio.html")
        else:

            mi_formulario = formularioAvatar()
            editAvatar = False

        return render(request, "editarAvatar.html", {"miFormulario": mi_formulario, "usuario": usuario, "editAvatar": editAvatar, "imagen": imagen_avatar})