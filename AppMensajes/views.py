from django.shortcuts import render
from AppMensajes.models import *
from AppUsuarios.models import *
from django.contrib.auth.models import User

# Create your views here.
def messages(request):

    conversacion = list(mensajes.objects.filter())
    usuarios = list(User.objects.filter())
    contexto = {"conversacion": conversacion, "usuarios": usuarios, "logueado": request.user.username}
    print(type(contexto['logueado']))
    print(type(contexto['usuarios'][0]))

    return render(request, "messages.html", contexto)


def chat(request, receptor):

    if request.method == 'GET':
        contexto = {"mensaje": f"usted quiere chatear con {receptor}"}

    return render(request, "chat.html", contexto)    

