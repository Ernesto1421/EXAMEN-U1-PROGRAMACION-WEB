from django.db import models
from ESTADIOS.models import Estadio

# Create your models here.

class Equipo(models.Model):
    Nombre = models.CharField(max_length=100)
    Estadio =  models.ForeignKey(Estadio, related_name='Estadio_de_equipo', on_delete=models.CASCADE,)
    Colonia = models.CharField(max_length=100)
    Patrocinador = models.CharField(max_length=100)
    Coach = models.CharField (max_length=100)

    def __str__(self):
            return self.Nombre
    def __unicode__(self):
            return self.Nombre

            
