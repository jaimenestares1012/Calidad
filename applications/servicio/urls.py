from django.contrib import admin
from django.urls import path
from . import views 

app_name = "servicio"
urlpatterns = [
    path('', views.prueba.as_view()),
    path('lista_servicios/', views.ListaServicios.as_view(), name="lista-servicios"),
    path('pasarella/<int:id>/', views.RealizarPago.as_view(), name="pasarella"),
    path('lista_recibos/', views.ListaRecibos.as_view(), name="lista-recibos"),
]
