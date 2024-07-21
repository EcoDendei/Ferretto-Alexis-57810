from django.contrib import admin

# Register your models here.
from .models import *

class MonedaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "sigla", "simbolo")

class AsientoAdmin(admin.ModelAdmin):
    list_display = ("fecha", "desc", "activo")
    list_filter = ("desc", "activo")

admin.site.register(Cuenta)
admin.site.register(Subcuenta)
admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Asiento, AsientoAdmin)
admin.site.register(Movimiento)
