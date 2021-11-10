from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.prueba.as_view()),
    path('lista_servicios/', views.ListaServicios.as_view(), name="lista-servicios"),
    path('pasarella/', views.RealizarPago.as_view(), name="pasarella"),
]
