from django.shortcuts import render
from AppBlog.forms import cargar_receta
from AppBlog.models import receta
import datetime
from django.conf import settings

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
        autor_usuario = f"{request.user}",
        autor_nombre = f"({request.user.first_name} {request.user.last_name})"
      )

      nueva_receta.save()
      recetaCargada = True

  else:
    cargar_receta_form = cargar_receta()
    recetaCargada = False

  contexto = {"cargarRecetaForm": cargar_receta_form, "recetaCargada": recetaCargada, "imagen": imagen_avatar}

  return render(request, "cargarReceta.html", contexto)


def verReceta(request, receta_id):

  imagen_avatar = list(avatar.objects.filter(user=request.user.id))
  verReceta = receta.objects.get(id=receta_id)
  usuario = request.user

  if imagen_avatar != []:
    contexto = {"usuario": str(usuario), "verReceta": verReceta, "imagen":imagen_avatar[0].imagen.url}  #-------> Cargar la imagen rompe el template

  else:
    contexto = {"usuario": str(usuario), "verReceta": verReceta, "imagen": "/Media/Avatares/dummy-avatar.jpg"}

  return render(request, "verReceta.html", contexto)


@login_required
def editarReceta(request, receta_id):

  imagen_avatar = list(avatar.objects.filter(user=request.user.id))
  contexto = {}

  if imagen_avatar != []:
    contexto.update(imagen = imagen_avatar[0].imagen.url)

  else:
    contexto.update(imagen = "/Media/Avatares/dummy-avatar.jpg")


  if request.method == 'GET':
    print('entre a la funcion editarReceta GET')

    bla = receta.objects.get(id=receta_id)
    contexto.update(receta_id=receta_id)
    contexto.update(receta = bla)
    contexto.update(editarReceta = False)

    initialValues = {
                      "nombre_receta": bla.nombre_receta,
                      "descripcion_receta": bla.descripcion_receta,
                      "receta": bla.receta,
                      "imagen" : bla.imagen

                  }

    mi_formulario = cargar_receta(initial=initialValues)

    contexto.update(miFormulario=mi_formulario)
    contexto.update(receta_id=receta_id)

  return render(request, "editarReceta.html", contexto)


def editadaReceta(request):

  imagen_avatar = list(avatar.objects.filter(user=request.user.id))
  contexto = {}

  if imagen_avatar != []:
    contexto.update(imagen = imagen_avatar[0].imagen.url)

  else:
    contexto.update(imagen = "/Media/Avatares/dummy-avatar.jpg")

  if request.method == 'POST':

    receta_id = request.POST['receta_id']
    receta_a_editar = receta.objects.get(id=receta_id)
    
    mi_formulario = cargar_receta(request.POST, request.FILES)
    print(mi_formulario)
    mi_formulario = mi_formulario.cleaned_data
    print(mi_formulario)
    
    receta_a_editar.nombre_receta = mi_formulario['nombre_receta']
    receta_a_editar.descripcion_receta = mi_formulario['descripcion_receta']
    receta_a_editar.receta = mi_formulario['receta']

    if mi_formulario['imagen'] != (None or False):
      receta_a_editar.imagen = mi_formulario['imagen']      
    else:
      receta_a_editar.imagen = 'Recetas/dummy.jpg'
    
    receta_a_editar.save()
    contexto.update(mensaje = 'Receta actualizada!!!')
    contexto.update(editadaReceta = True)
    contexto.update(receta_id = receta_id)

  else:
    contexto.update(mensaje = 'Ocurrio algun error, no se actualizo la receta.')
    contexto.update(editadaReceta = False)

  return render(request, "editadaReceta.html", contexto)