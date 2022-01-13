from django.shortcuts import render
from paginas.models import TratamientoOdontologico
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    # return HttpResponse("Esto es una prueba del inicio")
    tratamientos = TratamientoOdontologico.objects.all().order_by('-fecha')[:5]
    return render(request, 'paginas/inicio.html', {"tratamientos": tratamientos})
def inicioPaginas(request):
    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'paginas/paginas.html')
def about(request):
    return render(request, 'paginas/about.html')

class TratamientosOdontologicosList(ListView):
    
    model = TratamientoOdontologico
    template_name = "paginas/listaTratamientos.html"

class TratamientosOdontologicosDetalle(DetailView):
    
    model = TratamientoOdontologico
    template_name = "paginas/detalleTratamientos.html"

class TratamientosOdontologicosCreacion(CreateView):
    
    model = TratamientoOdontologico
    success_url = "/pages/listaTratamientos/" 
    fields = ["tratamiento", "contenido", "autor", "fecha"]
     
class TratamientosOdontologicosUpdate(UpdateView):
    
    model = TratamientoOdontologico
    success_url = "../listaTratamientos/"
    fields = ["tratamiento", "contenido", "autor", "fecha"]
  
class TratamientosOdontologicosDelete(DeleteView):
    
    model = TratamientoOdontologico
    success_url = "../listaTratamientos/"