from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from accounts.models import Avatar
from accounts.forms import UserRegisterForm, AvatarFormulario, UserEditForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from paginas.models import TratamientoOdontologico

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
        
        tratamientos = TratamientoOdontologico.objects.all().order_by('-fecha')[:5]
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "paginas/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!", "tratamientos" : tratamientos})
                
            else:
                
                return render(request, "paginas/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!","tratamientos" : tratamientos})
                
            
        else:
            
            return render(request, "paginas/inicio.html", {"mensaje":f"FORMULARIO erroneo","tratamientos" : tratamientos})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "accounts/login.html", {"form":form} )



def register(request):

      if request.method == 'POST':
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                userid = User.objects.get(username=username)
                grupo = Group.objects.get(name='Grupo1')
                grupo.user_set.add(userid)

                  
                tratamientos = TratamientoOdontologico.objects.all().order_by('-fecha')[:5]
                return render(request, "paginas/inicio.html", {"mensaje":f"{username} Creado :)", "tratamientos" : tratamientos})

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
                  tratamientos = TratamientoOdontologico.objects.all().order_by('-fecha')[:5]
                  return render(request, "paginas/inicio.html", {"tratamientos" : tratamientos})

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})

@login_required
def editarPerfil(request):
    usuario = request.user
    
    if( request.method == "POST" ):
        miFormulario = UserEditForm(request.POST)
        
        if( miFormulario.is_valid()):
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.save()
            tratamientos = TratamientoOdontologico.objects.all().order_by('-fecha')[:5]
            return render(request, "paginas/inicio.html", {"mensaje":f"Perfil editado :)", "tratamientos" : tratamientos})

    else:
        miFormulario = UserEditForm(initial={"email": usuario.email})
    
    return render(request, "accounts/editarPerfil.html", {"miFormulario":miFormulario, "usuario": usuario})

def eliminarPerfil(request):
    usuarioBorrar = User.objects.get(username=request.user.username)
    logout(request)
    usuarioBorrar.delete()
    
    tratamientos = TratamientoOdontologico.objects.all().order_by('-fecha')[:5]
    
    return render(request, "paginas/inicio.html", {"mensaje":f"Eliminación de perfil exitosa", "tratamientos" : tratamientos})