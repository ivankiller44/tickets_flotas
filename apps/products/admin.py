from django.contrib import admin
from apps.products.models import * 

# Register your models here.

admin.site.register(Origen)
admin.site.register(Destino)
admin.site.register(TipoDeBus)
admin.site.register(NumeroDeBus)
admin.site.register(FechaDeSalida)
admin.site.register(HoraDeSalida)
admin.site.register(Viaje)
