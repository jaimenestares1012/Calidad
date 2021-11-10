from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.prueba.as_view()),
    path('lista-actividades/', views.ListaActividades.as_view()),
    
]
