from django.urls import path
from EQUIPOS import views
urlpatterns = [
     path('', views.index,name= "index"),

]