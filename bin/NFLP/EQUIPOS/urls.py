from django.urls import path
from EQUIPOS import views
urlpatterns = [
     path('', views.index,name= "Index"),
     path('listar', views.equipos_list, name= "Index"),

]
