from django.shortcuts import render
from AppMensajes.forms import *
from AppMensajes.models import *
from AppUsuarios.models import *
from AppUsuarios.forms import *
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required

FECHA_ACTUAL = datetime.datetime.now()

# Create your views here.
@login_required
def messages(request):

    imagen_avatar = list(avatar.objects.filter(user=request.user.id))

    if imagen_avatar != []:
        imagen_avatar = imagen_avatar[0].imagen.url
    else:
        imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

    conversacion = list(mensajes.objects.filter())
    usuarios = list(User.objects.filter())
    contexto = {"imagen": imagen_avatar, "conversacion": conversacion, "usuarios": usuarios, "logueado": request.user.username}

    return render(request, "messages.html", contexto)

@login_required
def chat(request):
    
    imagen_avatar = list(avatar.objects.filter(user=request.user.id))

    if imagen_avatar != []:
        imagen_avatar = imagen_avatar[0].imagen.url
    else:
        imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

    if request.method == 'POST':
        contexto = {"imagen": imagen_avatar, "receptor": request.POST['receptor']}

    return render(request, "chat.html", contexto)


@login_required
def chatEnviar(request, receptor):

    imagen_avatar = list(avatar.objects.filter(user=request.user.id))

    if imagen_avatar != []:
        imagen_avatar = imagen_avatar[0].imagen.url
    else:
        imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

    if request.method == 'GET':

        enviar_mensaje_form = enviar_mensaje(initial = {"receptor": receptor})
        volver_form = volver_opciones_mensaje(initial = {"receptor": receptor})
        mensajeEnviado = False


    if request.method == 'POST':

        enviar_mensaje_form = enviar_mensaje(request.POST)

        if enviar_mensaje_form.is_valid:
            print(enviar_mensaje_form)
            enviar_mensaje_cleaned = enviar_mensaje_form.cleaned_data

            nuevo_mensaje = mensajes(
            fecha = f"{FECHA_ACTUAL.year}-{FECHA_ACTUAL.month}-{FECHA_ACTUAL.day} {FECHA_ACTUAL.hour}:{FECHA_ACTUAL.minute}:{FECHA_ACTUAL.second}",
            emisor = request.user,
            receptor = enviar_mensaje_cleaned["receptor"],
            cuerpo = enviar_mensaje_cleaned["cuerpo"],
            leido = False
            )

            nuevo_mensaje.save()
            mensajeEnviado = True
            enviar_mensaje_form = enviar_mensaje(initial = {"receptor": receptor})
            volver_form = volver_opciones_mensaje(initial = {"receptor": receptor})

    contexto = {"imagen": imagen_avatar, "receptor": receptor, "enviar_mensaje_form": enviar_mensaje_form, "mensajeEnviado": mensajeEnviado, "volver_form": volver_form}

    return render(request, "chatEnviar.html", contexto)
    

@login_required
def chatRecibir(request, receptor):

    imagen_avatar = list(avatar.objects.filter(user=request.user.id))

    if imagen_avatar != []:
        imagen_avatar = imagen_avatar[0].imagen.url
    else:
        imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

    if request.method == 'GET':
        usuario = request.user.username
        todosLosMensajes = mensajes.objects.filter(emisor=request.user.username, receptor=receptor) | mensajes.objects.filter(emisor=receptor, receptor=request.user.username)
        todosLosMensajesOrdenados = todosLosMensajes.order_by('-fecha')
        volver_form = volver_opciones_mensaje(initial = {"receptor": receptor})

        contexto = {"imagen": imagen_avatar, "volver_form": volver_form, "receptor": receptor, "usuario": usuario, "todosLosMensajes": todosLosMensajesOrdenados}


    return render(request, "chatRecibir.html", contexto)

