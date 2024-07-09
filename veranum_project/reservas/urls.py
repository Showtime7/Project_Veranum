from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hoteles/', views.lista_hoteles, name='lista_hoteles'),
]
