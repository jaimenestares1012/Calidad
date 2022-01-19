from django.contrib import admin
from django.urls import path
from . import views

# de define el nomnbre de las urls globales
app_name = "mantenimiento"
# se crean los urls patterms
urlpatterns = [
# crea path por path
    path('', views.prueba.as_view()),
    path('lista-mantenimiento/<shorname>',
         views.ListaMantenimiento.as_view(),name="lista-mantenimiento"),
    path('crear-mantenimiento/',
         views.mantenimiento_view.as_view(),name="crear-mantenimiento"),
    path('mis-mantenimientos/',
         views.ListaMantenimientosPropias.as_view(), name="mis-mantenimiento"),
    path('add_externos/<shorname>',
         views.ExternosView.as_view(), name="add-externos"),
    path('list_externos/<shorname>',
         views.list_externos.as_view(), name="list-externos"),
]
