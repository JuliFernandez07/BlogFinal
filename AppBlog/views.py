from django.shortcuts import render
from AppBlog.forms import cargar_receta

from AppBlog.models import receta

def inicio(request):
  return render(request, 'Inicio.html')

def fulano(request):
    return render(request, "Inicio.html")

def cargarReceta(request):
    if request.method == 'POST':
        cargar_receta_form = cargar_receta(request.POST)
        print(cargar_receta_form)
        if cargar_receta_form.is_valid:
            cargar_receta_cleaned = cargar_receta_form.cleaned_data

            nueva_receta = receta(
                fecha = "2022-10-10",
                nombre_receta = cargar_receta_cleaned["nombre_receta"],
                imagen = cargar_receta_cleaned["imagen"],
                receta = cargar_receta_cleaned["receta"],
                autor = "Juli"
            )

            nueva_receta.save()

    else:
        cargar_receta_form = cargar_receta()

    contexto = {"cargar_receta_form": cargar_receta_form}


    return render (request, "cargarReceta.html", contexto)

def verReceta(request):
    return render(request, "verReceta.html")

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