from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Marca(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class TipoHerramienta(models.Model):
    description = models.CharField(max_length=255)

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

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart({self.user})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.nombre}"

    def total_price(self):
        return self.product.precio * self.quantity
