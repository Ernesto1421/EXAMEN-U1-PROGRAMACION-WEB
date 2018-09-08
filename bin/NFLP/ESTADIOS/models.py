from django.db import models

# Create your models here.
class Estadio(models.Model):
    stadium = models.CharField(max_length=100)
    Capacidad = models.IntegerField(default= 10000)


    def __str__(self):
            return self.stadium
    def __unicode__(self):
            return self.stadium
