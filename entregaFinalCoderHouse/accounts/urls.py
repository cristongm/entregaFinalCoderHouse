from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='Accounts'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),    
    path('logout', LogoutView.as_view(template_name='paginas/inicio.html'), name="Logout"), 
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('eliminarPerfil', views.eliminarPerfil, name="EliminarPerfil"),
]
