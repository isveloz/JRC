from django.db import models # type: ignore

# Create your models here.
class Marca(models.Model):
    descripcion = models.CharField(max_length=10)

    def __str__(self):
        return self.descripcion

class TipoHerramienta(models.Model):
    description = models.CharField(max_length=20)

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
    precio = models.IntegerField(default=0)  # Añadir valor predeterminado aquí

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, default='')  # Añadir valor predeterminado aquí
    apellidoP = models.CharField(max_length=50)
    apellidoM = models.CharField(max_length=50)
    puesto = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidoP} {self.apellidoM}"
