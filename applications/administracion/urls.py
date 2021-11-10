from django.contrib import admin
from django.urls import path
from . import views


app_name="administracion"

urlpatterns = [
    path('', views.prueba.as_view()),
    path('iniciar_sesion/', views.InicioSesion.as_view(), name="iniciar_sesion"),
]
