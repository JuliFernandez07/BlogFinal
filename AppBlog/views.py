from django.shortcuts import render
from AppBlog.forms import cargar_receta
from AppBlog.models import receta
import datetime

FECHA_ACTUAL = datetime.datetime.now()

def inicio(request):

  if request.method == 'GET':
    todasLasRecetas = list(receta.objects.all())[::-1]

  contexto = {'todasLasRecetas': todasLasRecetas}

  return render(request, "Inicio.html", contexto)


def cargarReceta(request):
  if request.method == 'POST':

    cargar_receta_form = cargar_receta(request.POST)

    if cargar_receta_form.is_valid:
      print(cargar_receta_form)
      cargar_receta_cleaned = cargar_receta_form.cleaned_data

      nueva_receta = receta(
        fecha = f"{FECHA_ACTUAL.year}-{FECHA_ACTUAL.month}-{FECHA_ACTUAL.day}",
        nombre_receta = cargar_receta_cleaned["nombre_receta"],
        imagen = cargar_receta_cleaned["imagen"],
        receta = cargar_receta_cleaned["receta"],
        autor = "Juli"
      )

      nueva_receta.save()
      recetaCargada = True

  else:
    cargar_receta_form = cargar_receta()
    recetaCargada = False

  contexto = {"cargarRecetaForm": cargar_receta_form, "recetaCargada": recetaCargada}

  return render (request, "cargarReceta.html", contexto)


def verReceta(request, receta_id):
  verReceta = receta.objects.get(id=receta_id)
  contexto = {"verReceta": verReceta}

  return render(request, "verReceta.html", contexto)

"""
def loadInstruments(request):

  if request.method == 'POST':

    newInstrumentForm = InstrumentsForm(request.POST)
    print(newInstrumentForm)

    if newInstrumentForm.is_valid:
      newInstrumentDict = newInstrumentForm.cleaned_data
      newInstrument = Instruments(
        type = newInstrumentDict['type'],
        brand = newInstrumentDict['brand'],
        model = newInstrumentDict['model']
      )

      newInstrument.save()
      instrumentoCargado = True

  else:
    newInstrumentForm = InstrumentsForm()
    instrumentoCargado = False

  return render(request, "loadInstruments.html", {"instrumentoCargado": instrumentoCargado, "newInstrumentForm": newInstrumentForm})
  """