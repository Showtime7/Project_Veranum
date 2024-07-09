
from django.shortcuts import render

def index(request):
    return render(request, 'reservas/index.html')

def lista_hoteles(request):
    return render(request, 'reservas/hoteles.html')

def contacto(request):
    return render(request, 'reservas/contacto.html')
