from django.contrib import admin
from .models import Marca, TipoProducto, Producto, CarritoItem

admin.site.register(Marca)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(CarritoItem)
