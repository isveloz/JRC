from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore

# Modelos

class Marca(models.Model):
    descripcion = models.CharField(max_length=255)  # Aumentar longitud máxima

    def __str__(self):
        return self.descripcion

class TipoHerramienta(models.Model):
    description = models.CharField(max_length=255)  # Aumentar longitud máxima

    def __str__(self):
        return self.description

class Genero(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo

class TipoEmpleado(models.Model):
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoHerramienta, on_delete=models.CASCADE)
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    precio = models.IntegerField(default=0)
    categoria = models.CharField(max_length=50, default='Sin categoría')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, default='')
    apellidoP = models.CharField(max_length=50)
    apellidoM = models.CharField(max_length=50)
    puesto = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellidoP} {self.apellidoM}"

# Crear y guardar objetos relacionados
def crear_objetos():
    # Crear y guardar tipo de herramienta
    tipo_herramienta = TipoHerramienta(description="Herramienta manual")
    tipo_herramienta.save()

    # Crear y guardar marca
    marca = Marca(descripcion="Marca de prueba")
    marca.save()

    # Crear y guardar producto
    producto = Producto(
        nombre="Producto de prueba",
        tipo=tipo_herramienta,
        descripcion="Este es un producto de prueba.",
        marca=marca,
        precio=10000,
        categoria="Prueba"
    )
    producto.save()

    # Verificar que el producto fue creado
    productos = Producto.objects.all()
    for prod in productos:
        print(f"ID: {prod.id}, Nombre: {prod.nombre}, Precio: {prod.precio}, Tipo: {prod.tipo.description}, Marca: {prod.marca.descripcion}")

# Ejecutar la función para crear los objetos
if __name__ == "__main__":
    crear_objetos()
