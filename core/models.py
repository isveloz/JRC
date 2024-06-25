from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from mysite import settings

class Marca(models.Model):
    nombre = models.CharField(max_length=255, default='Marca Predeterminada')

    def __str__(self):
        return self.nombre

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    Nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='producto', null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    añadido_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.Nombre}'

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

#PROCESOS
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default='pendiente')
    fecha = models.DateTimeField(auto_now_add=True)

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Boleta(models.Model):
    id_boleta = models.CharField(max_length=20, primary_key=True)
    cliente = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.id_boleta} - {self.cliente}"

#INFO
opciones_motivos = [
    [0, "reclamo"],
    [1, "sugerencia"],
    [2, "ayuda"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    motivo = models.IntegerField(choices=opciones_motivos)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre

#transaccion
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buy_order = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    authorization_code = models.CharField(max_length=50)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.buy_order} - {self.status}"