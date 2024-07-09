# en veranum_project/urls.py
from django.contrib import admin
from django.urls import path
from reservas import views as reservas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reservas_views.index, name='index'),
    path('hoteles/', reservas_views.lista_hoteles, name='lista_hoteles'),
    path('contacto/', reservas_views.contacto, name='contacto'),
]
