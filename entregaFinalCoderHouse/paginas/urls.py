from django.urls import path, re_path
from paginas import views

urlpatterns = [
    path('', views.inicioPaginas, name='Pages'),
    path('listaTratamientos/', views.TratamientosOdontologicosList.as_view(), name='listaTratamientos'),
    re_path(r'^(?P<pk>\d+)$', views.TratamientosOdontologicosDetalle.as_view(), name='detalleTratamientos'),
    path(r'^nuevo$', views.TratamientosOdontologicosCreacion.as_view(), name='newTratamientos'),
    re_path(r'^editar/(?P<pk>\d+)$', views.TratamientosOdontologicosUpdate.as_view(), name='editTratamientos'),
    re_path(r'^borrar/(?P<pk>\d+)$', views.TratamientosOdontologicosDelete.as_view(), name='deleteTratamientos'),
]
