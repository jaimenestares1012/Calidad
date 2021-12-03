from django.contrib import admin
from django.urls import path
from . import views

app_name = "visita"
urlpatterns = [
    path('prueba/', views.prueba.as_view(), name="lista_visita"),
    path('add/', views.visitaCreateView.as_view(), name="add_visita"),
    path('add_visitantes/<shorname>', views.visitantesCreateView.as_view(), name="add_visitantes")
]
