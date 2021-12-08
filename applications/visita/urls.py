from django.contrib import admin
from django.urls import path
from . import views

app_name = "visita"
urlpatterns = [
    path('prueba/', views.prueba.as_view(), name="lista_visita"),
    path('add/', views.visita_view.as_view(), name="add_visita"),
    path('add_visitantes/<int:shorname>/', views.visitantes_view.as_view(), name="add_visitantes"),
    path('list_visitantes/<int:shorname>/',
         views.list_visitantes.as_view(), name="list_visitantes")
]
