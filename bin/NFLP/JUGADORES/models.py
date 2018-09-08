from django.db import models
from EQUIPOS.models import Equipo

# Create your models here.


class Jugador(models.Model):
    Nombre_jugador = models.CharField(max_length=100)
    Equipo_jugador =  models.ForeignKey(Equipo, related_name='Equipo_de_jugador', on_delete=models.CASCADE,)
    Edad = models.IntegerField()
    Numero = models.IntegerField()
    Posicion = models.CharField (max_length=100)
    Altura_cm = models.IntegerField(default=180)
    Peso_Kg =models.IntegerField(default= 80)


    def __str__(self):
            return self.Nombre_jugador
    def __unicode__(self):
            return self.Nombre_jugador