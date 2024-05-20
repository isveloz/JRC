from django.contrib import admin # type: ignore

from core.models import Empleado, Genero, Marca, Producto, TipoEmpleado, TipoHerramienta # type: ignore

# Register your models here.
admin.site.register(Marca)
admin.site.register(TipoHerramienta)
admin.site.register(Genero)
admin.site.register(TipoEmpleado)
admin.site.register(Producto)
admin.site.register(Empleado)