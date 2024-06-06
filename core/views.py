from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import requests
from .forms import ClienteForm, UserRegisterForm, TareaForm
from .models import Cliente, Pedido, PedidoItem, Producto, CarritoItem, Tarea
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.webpay.webpay_plus.transaction import Transaction as WebpayTransaction
from .models import Transaction

# Páginas principales
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contacto(request):
    return render(request, 'core/contacto.html')

# Autenticación de usuarios
def colaborador_login(request):
    return render(request, 'core/colaborador_login.html')

def cliente_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'core/cliente_login.html')

def bodeguero_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'core/bodeguero_login.html')

def contador_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'core/contador_login.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cliente.objects.create(user=user)  # Crear Cliente asociado al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Cuenta creada para {username}')
                return redirect('home')
            else:
                messages.error(request, 'Ocurrió un problema al autenticar el usuario.')
        else:
            print(form.errors)  # Añadir esto para ver los errores del formulario en la consola
            messages.error(request, 'Corrige los errores en el formulario')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

# Gestión del carrito
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, created = CarritoItem.objects.get_or_create(producto=producto)
    if not created:
        carrito_item.cantidad += 1
    carrito_item.save()
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(CarritoItem, id=item_id)
    carrito_item.delete()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito_items = CarritoItem.objects.all()
    return render(request, 'core/ver_carrito.html', {'carrito_items': carrito_items})

@login_required
def checkout(request):
    carrito_items = CarritoItem.objects.all()
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    return render(request, 'core/checkout.html', {'carrito_items': carrito_items, 'total': total})

@login_required
def procesar_pago(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        tarjeta = request.POST.get('tarjeta')
        expiracion = request.POST.get('expiracion')
        cvv = request.POST.get('cvv')
        
        messages.success(request, 'Pago procesado correctamente')
        
        return redirect('pago_exitoso')
    
    return redirect('checkout')

@login_required
def pago_exitoso(request):
    return render(request, 'core/pago_exitoso.html')

# Gestión de productos
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/productos.html', {'productos': productos})

def product_detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'core/product_detail.html', {'producto': producto})

# Gestión de tareas
@login_required
def listar_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'core/listar_tareas.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            messages.success(request, 'Tarea creada con éxito')
            return redirect('listar_tareas')
    else:
        form = TareaForm()
    return render(request, 'core/crear_tarea.html', {'form': form})

@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada con éxito')
            return redirect('listar_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'core/editar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada con éxito')
        return redirect('listar_tareas')
    return render(request, 'core/eliminar_tarea.html', {'tarea': tarea})

# Gestión de clientes
@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
            cliente.save()
            messages.success(request, 'Cliente creado con éxito')
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'core/crear_cliente.html', {'form': form})

@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado con éxito')
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/editar_cliente.html', {'form': form})

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/listar_clientes.html', {'clientes': clientes})

    add_form = ProductoForm()

    return render(request, 'app/CRUD/bodeguero.html', {
        'pedidos': pedidos,
        'productos': productos,
        'form': form,
        'edit_producto_id': edit_producto_id,
        'add_form': add_form,
        'marcas': marcas,
    })

def contador(request):
    if request.method == 'POST':
        form = BoletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contador')
    else:
        form = BoletaForm()
    boletas = boletas.objects.all()
    return render(request, 'app/CRUD/contador.html', {'form': form, 'boletas': boletas})

def ingreso_boletas(request):
    if request.method == 'POST':
        form = BoletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contador')
    else:
        form = BoletaForm() # type: ignore
    return render(request, 'app/CRUD/contador.html', {'form': form})

def pago_iniciar(request):
    # Obtén el carrito del usuario con estado 'pendiente'
    carrito_items = CarritoItem.objects.all()

    # Calcula el total del carrito
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    
    # Redondea el total a un entero
    total = int(total)

    # Configura la transacción de Webpay
    tx = WebpayTransaction()
    response = tx.create(
        buy_order=str(request.user.id) + str(carrito_items.first().id),
        session_id=request.session.session_key,
        amount=total,
        return_url="http://127.0.0.1:8000/pago_exito/"
    )

    if request.method == 'POST':
        # Crear el pedido después de confirmar el pago
        pedido = Pedido.objects.create(user=request.user, total=total)
        for item in carrito_items:
            PedidoItem.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.producto.precio
            )
        for item in carrito_items:
            item.delete()

        return redirect('pago_exito')

    return render(request, 'core/pago_iniciar.html', {'response': response, 'total': total})

def pago_exito(request):
    token = request.GET.get('token_ws')
    tx = WebpayTransaction()
    response = tx.commit(token)
    
    if response['response_code'] == 0:  # Transacción exitosa
        # Guardar la transacción en la base de datos
        Transaction.objects.create(
            user=request.user,
            buy_order=response['buy_order'],
            session_id=response['session_id'],
            amount=response['amount'],
            status=response['status'],
            authorization_code=response['authorization_code']
        )
        
        return render(request, 'core/pago_exitoso.html', {'response': response})
    else:
        return render(request, 'core/pago_error.html', {'response': response})

def pago_exito(request):
    token = request.GET.get('token_ws')
    tx = WebpayTransaction()
    response = tx.commit(token)
    
    if response['response_code'] == 0:  # Transacción exitosa
        # Guardar la transacción en la base de datos
        Transaction.objects.create(
            user=request.user,
            buy_order=response['buy_order'],
            session_id=response['session_id'],
            amount=response['amount'],
            status=response['status'],
            authorization_code=response['authorization_code']
        )
        
        return render(request, 'core/pago_exitoso.html', {'response': response})
    else:
        return render(request, 'core/pago_error.html', {'response': response})