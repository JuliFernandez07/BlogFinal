from django.shortcuts import render
from AppBlog.forms import cargar_receta
from AppBlog.models import receta
import datetime

#Decorador por defecto
from django.contrib.auth.decorators import login_required
from AppUsuarios.models import avatar

FECHA_ACTUAL = datetime.datetime.now()

def about(request):

  imagen_avatar = list(avatar.objects.filter(user=request.user.id))
  
  if imagen_avatar != []:
    imagen_avatar = imagen_avatar[0].imagen.url
  else:
    imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

  contexto = {"imagen": imagen_avatar}

  return render(request, "about.html", contexto)

def inicio(request):
  
  imagen_avatar = list(avatar.objects.filter(user=request.user.id))

  if request.method == 'GET':
    todasLasRecetas = list(receta.objects.all())[::-1]

  if imagen_avatar != []:
    contexto = {'todasLasRecetas': todasLasRecetas, "imagen":imagen_avatar[0].imagen.url}
  
  else:
    contexto = {'todasLasRecetas': todasLasRecetas, "imagen": "/Media/Avatares/dummy-avatar.jpg"}

  return render(request, "Inicio.html", contexto)


@login_required
def cargarReceta(request):
    
  imagen_avatar = list(avatar.objects.filter(user=request.user.id))
  
  if imagen_avatar != []:
    imagen_avatar = imagen_avatar[0].imagen.url
  else:
    imagen_avatar = "/Media/Avatares/dummy-avatar.jpg"

  if request.method == 'POST':

    cargar_receta_form = cargar_receta(request.POST, request.FILES)

    if cargar_receta_form.is_valid:
      print(cargar_receta_form)
      cargar_receta_cleaned = cargar_receta_form.cleaned_data
        
      nueva_receta = receta(
        fecha = f"{FECHA_ACTUAL.year}-{FECHA_ACTUAL.month}-{FECHA_ACTUAL.day}",
        nombre_receta = cargar_receta_cleaned["nombre_receta"],
        imagen = cargar_receta_cleaned["imagen"],
        receta = cargar_receta_cleaned["receta"],
        autor = f"{request.user} ({request.user.first_name} {request.user.last_name})"
      )

      nueva_receta.save()
      recetaCargada = True

  else:
    cargar_receta_form = cargar_receta()
    recetaCargada = False

  contexto = {"cargarRecetaForm": cargar_receta_form, "recetaCargada": recetaCargada, "imagen": imagen_avatar}

  return render(request, "cargarReceta.html", contexto)



# @login_required
def verReceta(request, receta_id):

  imagen_avatar = list(avatar.objects.filter(user=request.user.id))
  verReceta = receta.objects.get(id=receta_id)

  if imagen_avatar != []:
    contexto = {"verReceta": verReceta, "imagen":imagen_avatar[0].imagen.url}  #-------> Cargar la imagen rompe el template

  else:
    contexto = {"verReceta": verReceta, "imagen": "/Media/Avatares/dummy-avatar.jpg"}

  return render(request, "verReceta.html", contexto)
