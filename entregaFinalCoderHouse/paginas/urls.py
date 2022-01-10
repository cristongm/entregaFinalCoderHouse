from django.urls import path, re_path
from paginas import views

urlpatterns = [
    path('', views.inicioPaginas, name='Pages'),
    path('listaTratamientos/', views.TratamientosOdontologicosList.as_view(), name='listaTratamientos'),
    re_path(r'^(?P<pk>\d+)$', views.TratamientosOdontologicosDetalle.as_view(), name='detalleTratamientos'),
]
