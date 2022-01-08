from django.db import models

# Create your models here.


class TratamientoOdontologico(models.Model):

    tratamiento = models.CharField(max_length=40)
    contenido = models.CharField(max_length=400)
    autor = models.CharField(max_length=40)
    fecha = models.DateField()