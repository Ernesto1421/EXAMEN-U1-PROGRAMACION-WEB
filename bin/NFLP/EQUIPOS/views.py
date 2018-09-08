from __future__ import unicode_literals

from django.shortcuts import render
from EQUIPOS.models import Equipo

# Create your views here.
def index (request):
    return render(request, "EQUIPOS/Index.html")

def equipos_list(request):
    equi= Equipo.objects.all()
    contexto = {'equi': Equipo}
    return render(request, 'EQUIPOS/Index.html', contexto)

