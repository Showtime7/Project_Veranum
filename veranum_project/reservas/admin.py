from django.contrib import admin
from .hotel import Hotel
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'hotel', 'fecha_entrada', 'fecha_salida', 'precio_total')
    readonly_fields = ('precio_total',)

    def save_model(self, request, obj, form, change):
        obj.precio_total = obj.calcular_precio_total()
        super().save_model(request, obj, form, change)

admin.site.register(Hotel)
admin.site.register(Reserva, ReservaAdmin)
