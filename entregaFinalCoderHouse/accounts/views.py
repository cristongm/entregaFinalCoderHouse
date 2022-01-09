from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from accounts.models import Avatar
from accounts.forms import UserRegisterForm, AvatarFormulario
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView


def inicio(request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url 
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html', diccionario)


def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "paginas/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
                
            else:
                
                return render(request, "paginas/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!"})
                
            
        else:
            
            return render(request, "paginas/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "accounts/login.html", {"form":form} )



def register(request):

      if request.method == 'POST':
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                  
                return render(request,"paginas/inicio.html" ,  {"mensaje":f"{username} Creado :)"})


      else:
                     
           form = UserRegisterForm()     

      return render(request,"accounts/register.html" ,  {"form":form})
 

@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})