from django import forms
from django.contrib.auth import get_user_model


class FormMensajes(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escribe tu mensaje', "rows":"4"}))
