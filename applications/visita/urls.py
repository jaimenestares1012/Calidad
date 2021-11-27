from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.prueba.as_view()),
    path('add/', views.visitaCreateView.as_view(), name="add_visita")
]
