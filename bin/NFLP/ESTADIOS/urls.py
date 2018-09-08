from django.urls import path
from ESTADIOS import views
urlpatterns = [
     path('', views.index,name= "index"),

]