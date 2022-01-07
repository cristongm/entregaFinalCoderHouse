from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'paginas/inicio.html')
def inicioPaginas(request):
    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'paginas/paginas.html')
def about(request):
    return render(request, 'paginas/about.html')