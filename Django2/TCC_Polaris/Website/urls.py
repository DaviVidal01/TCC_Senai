from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes_fotos/', views.detalhes_fotos, name='detalhes_fotos'),
    path('dashboard/', views.dashboard, name='dashboard'),
]