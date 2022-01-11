from django.contrib import admin
from django.urls import path
from . import views


app_name = "mantenimiento"
urlpatterns = [
    path('', views.prueba.as_view()),
    path('lista-mantenimiento/<shorname>',
         views.ListaMantenimiento.as_view(),name="lista-mantenimiento"),
    path('crear-mantenimiento/',
         views.mantenimiento_view.as_view(),name="crear-mantenimiento"),
    path('mis-mantenimientos/',
         views.ListaMantenimientosPropias.as_view(), name="mis-mantenimiento"),
]
