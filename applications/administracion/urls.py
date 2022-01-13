from django.contrib import admin
from django.urls import path
from . import views

# definimos el nombre de los urls
app_name="administracion"


# definismo olos urls patterns que usarmos 
urlpatterns = [
    path('', views.prueba.as_view()),
    path('iniciar_sesion/', views.InicioSesion.as_view(), name="iniciar_sesion"),
]
