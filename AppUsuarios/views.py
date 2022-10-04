from django.shortcuts import render
from AppUsuarios.forms import *

# Create your views here.
def register(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return render(request,"inicioRegister.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        #form = UserCreationForm()       
        form = RegisterForm()     

    return render(request,"register.html" ,  {"form": form})



def logout(request):

    # logout(request)
    messages.info(request, "Saliste sin problemas")

    return redirect("inicio")
     

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
    
            if user is not None:
                login(request, user)
                
                return render(request,"AppUsuarios/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )

            else:
                return render(request,"AppUsuarios/inicio.html", {"mensaje":"Error, datos incorrectos"} )

        else:
            return render(request,"AppUsuarios/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppUsuarios/login.html", {'form':form})
