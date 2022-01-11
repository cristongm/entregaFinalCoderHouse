from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import CanalMensaje, CanalUsuario, Canal
from .forms import FormMensajes
from django.apps import apps
from django.views.generic.edit import FormMixin
# Create your views here.
@login_required
def inicio(request):
    inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])
    usuarios = apps.get_model('auth', model_name='User').objects.all()
    context = {
        "inbox": inbox,
        "usuarios": usuarios
    }
    return render(request, 'mensajes/inicio.html', context)
class CanalFormMixin(FormMixin):
    form_class = FormMensajes
    #success_url = "./"
    def get_success_url(self):
        return self.request.path
    
    def post(self, request, *args, **kwargs):
        if(not request.user.is_authenticated):
            raise PermissionDenied
        form = self.get_form()
        if form.is_valid():
            canal = self.get_object()
            usuario = self.request.user
            mensaje = form.cleaned_data.get("mensaje")
            canal_obj = CanalMensaje.objects.create(canal=canal, usuario=usuario, texto=mensaje)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
class DetailMsg(LoginRequiredMixin, CanalFormMixin, DetailView):
    template_name = 'mensajes/canal_detail.html' 
    def get_object(self, *args, **kwargs):
        mi_username= self.request.user.username
        username = self.kwargs.get('username')
        
        print(username)
        print(mi_username)
        if(username == mi_username):
            mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)
            return mi_canal
        
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)
        if(canal == None):
            raise Http404
        return canal
        
def mensajes_privados(request,username, *args, **kwargs):
    if (not request.user.is_authenticated):
        return HttpResponse("Prohibido")
    mi_username = request.user.username
    print(mi_username)
    canal, created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)
    if created:
        print("Si, fue creado")
    
    Usuarios_Canal = canal.canalusuario_set.all().values("usuario__username")
    print(Usuarios_Canal)
    mensaje_canal = canal.canalmensaje_set.all()
    print(mensaje_canal.values("texto"))
    
    return HttpResponse(f"Nuestro ID Canal - {canal.id}")