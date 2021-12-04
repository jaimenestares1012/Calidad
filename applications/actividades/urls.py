from django.contrib import admin
from django.urls import path
from . import views


app_name = "actividades"
urlpatterns = [
    path('', views.prueba.as_view()),
    path('lista-actividades/<shorname>',
         views.ListaActividades.as_view(),name="lista-actividades"),
    path('crear-actividades/', views.ActividadesCreateView.as_view()),
    path('success/', views.Success.as_view() , name="success"),
    path('mis-actividades/<shorname>',
         views.ListaActividadesPropias.as_view(), name="mis-actividades"),
    
]
