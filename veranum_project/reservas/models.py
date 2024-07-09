from django.db import models
from .hotel import Hotel  # Importa el modelo Hotel desde hotel.py

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    servicios_extra = models.CharField(max_length=200, blank=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calcular_precio_total(self):
        dias = (self.fecha_salida - self.fecha_entrada).days
        precio_base = self.hotel.precio_por_noche * dias
        precio_servicios = 0
        if 'masaje' in self.servicios_extra:
            precio_servicios += 50000
        if 'sauna' in self.servicios_extra:
            precio_servicios += 50000
        return precio_base + precio_servicios

    def save(self, *args, **kwargs):
        self.precio_total = self.calcular_precio_total()
        super().save(*args, **kwargs)
