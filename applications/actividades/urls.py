from django.contrib import admin
from django.urls import path
from . import views

# se hace la creacion de las urls disponibles
# se pone por nombbre actividades
app_name = "actividades"
# se crea los urls pattens
urlpatterns = [
     # creacion de los paths
    path('', views.prueba.as_view()),
    path('lista-actividades/<shorname>',
         views.ListaActividades.as_view(),name="lista-actividades"),
    path('crear-actividades/', views.ActividadesCreateView.as_view()),
    path('success/', views.Success.as_view() , name="success"),
    path('mis-actividades/<shorname>',
         views.ListaActividadesPropias.as_view(), name="mis-actividades"),
    
]
