from django.shortcuts import render

# Create your views here.
def inicio(request):
    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'accounts/inicio.html')