from django.contrib import admin
from django.urls import path
from . import views


app_name = "mantenimiento"
urlpatterns = [
    path('', views.prueba.as_view()),
    path('lista-mantenimiento/',
         views.ListaMantenimiento.as_view(),name="lista-mantenimiento"),
]
