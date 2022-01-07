from django.urls import path
from paginas import views

urlpatterns = [
    path('', views.inicioPaginas, name='Pages'),
]
