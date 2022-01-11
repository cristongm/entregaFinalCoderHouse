from django.urls import path
from mensajes import views

urlpatterns = [
    path('', views.inicio, name='Messages'),
    path("<str:username>", views.mensajes_privados),
    path("ms/<str:username>", views.DetailMsg.as_view(), name="DetailMsg"),
    
]
