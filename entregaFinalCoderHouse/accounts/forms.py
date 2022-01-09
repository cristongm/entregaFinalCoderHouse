from django import forms
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

    
    
class AvatarFormulario(forms.Form):

    #Especificar los campos
    
    imagen = forms.ImageField(required=True)