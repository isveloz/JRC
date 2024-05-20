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
    tipo= models.CharField(max_length=10)
    
    def __str__(self):
        return self.tipo

class TipoEmpleado(models.Model):
    tipo=models.CharField(max_length=15)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    Nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoHerramienta, on_delete=models.CASCADE)
    descripcion = models.TextField()  
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="noticias", null=True)
    precio = models.IntegerField

    def __str__(self):
        return self.Nombre


class Empleado(models.Model):
    rut= models.CharField (max_length=50)
    Nombre = models.CharField(max_length=50)
    apellidoP=models.CharField(max_length=50)
    apellidoM=models.CharField(max_length=50)
    puesto = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombre


