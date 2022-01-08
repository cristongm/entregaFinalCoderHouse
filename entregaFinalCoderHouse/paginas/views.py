from django.shortcuts import render
from paginas.models import TratamientoOdontologico
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'paginas/inicio.html')
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