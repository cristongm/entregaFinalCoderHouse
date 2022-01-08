from django.urls import path
from paginas import views

urlpatterns = [
    path('', views.inicioPaginas, name='Pages'),
    path('listaTratamientos/', views.TratamientosOdontologicosList.as_view(), name='listaTratamientos'),
    path(r'^(?P<pk>\d+)$', views.TratamientosOdontologicosDetalle.as_view(), name='detalleTratamientos'),
]
