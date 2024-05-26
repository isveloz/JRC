from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Producto, Cart, CartItem
from .forms import ContactoForm, RegistroForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.utils import timezone
from .models import Marca, TipoHerramienta, Genero, TipoEmpleado, Empleado
import locale  # Asegurarse de importar el módulo locale
from django.core.exceptions import ObjectDoesNotExist

# Configurar la localización para CLP
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

@login_required
def add_to_cart(request, product_id):
    try:
        producto = get_object_or_404(Producto, id=product_id)
        carrito, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=carrito, product=producto)
        cart_item.quantity += 1
        cart_item.save()
        return JsonResponse({'status': 'success'})
    except ObjectDoesNotExist as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'An unexpected error occurred'})

# Otras funciones de carrito
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart_view')

@login_required
def cart_view(request):
    carrito, created = Cart.objects.get_or_create(user=request.user)
    items_carrito = carrito.items.all()
    sub_total_items = sum(item.quantity * item.product.precio for item in items_carrito)
    total = sum(item.total_price() for item in items_carrito)
    total_formateado = locale.format_string("%d", total, grouping=True)

    ctx = {
        'items_carrito': items_carrito,
        'total': total,
        'total_formato': total_formateado,
        'sub_total': sub_total_items
    }
    return render(request, 'core/cart.html', ctx)

@login_required
def eliminar_del_carrito(request, id_item):
    cart_item = get_object_or_404(CartItem, id=id_item, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart_view')

@login_required
def vaciar_carrito(request):
    carrito = get_object_or_404(Cart, user=request.user)
    carrito.items.all().delete()
    messages.success(request, 'Cart has been emptied.')
    return redirect('cart_view')

@login_required
def aumentar_cantidad(request, id_item):
    cart_item = get_object_or_404(CartItem, id=id_item)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')

@login_required
def disminuir_cantidad(request, id_item):
    cart_item = get_object_or_404(CartItem, id=id_item)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

# Otras vistas existentes
def buscar_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(categoria__icontains(query)) # type: ignore
        )
    else:
        productos = Producto.objects.all()

    return render(request, 'core/buscar_productos.html', {'productos': productos, 'query': query})

def calcular_precio(request):
    try:
        cantidad = int(request.GET.get('cantidad', 1))
        precio_unitario = float(request.GET.get('precio_unitario', 0))
        total = cantidad * precio_unitario

        # Formatear el total en CLP
        total_clp = locale.format_string("%.0f", total, grouping=True)
        
        response_data = {'total': total_clp}
        return JsonResponse(response_data)
    except (TypeError, ValueError):
        # Manejar errores de tipo de datos incorrectos en la solicitud
        return JsonResponse({'error': 'Los parámetros cantidad y precio_unitario deben ser números válidos.'})

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def productos(request):
    productos_list = Producto.objects.all().order_by('nombre')
    paginator_instance = Paginator(productos_list, 6) # type: ignore
    page_number = request.GET.get('page')
    page_obj = paginator_instance.get_page(page_number)
    return render(request, 'core/productos.html', {'page_obj': page_obj})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            tipo_contacto = form.cleaned_data['tipo_contacto']

            # Enviar correo electrónico (configura el correo en settings.py)
            send_mail(
                asunto,
                f"Nombre: {nombre}\nCorreo: {correo}\nTeléfono: {telefono}\nTipo de contacto: {tipo_contacto}\n\nMensaje:\n{mensaje}",
                'tu_correo@example.com',
                ['destinatario@example.com'],
                fail_silently=False,
            )
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'core/contacto.html', {'form': form})

def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            tipo_contacto = form.cleaned_data['tipo_contacto']

            # Enviar correo electrónico (configura el correo en settings.py)
            send_mail(
                asunto,
                f"Nombre: {nombre}\nCorreo: {correo}\nTeléfono: {telefono}\nTipo de contacto: {tipo_contacto}\n\nMensaje:\n{mensaje}",
                'tu_correo@example.com',
                ['destinatario@example.com'],
                fail_silently=False,
            )
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('contacto')
    messages.error(request, 'Hubo un error al enviar tu mensaje. Por favor, intenta de nuevo.')
    return redirect('contacto')

def submit_newsletter_form(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        if correo:
            # Lógica para procesar la suscripción al boletín
            send_mail(
                'Suscripción al boletín',
                f"El correo {correo} se ha suscrito al boletín.",
                'tu_correo@example.com',
                ['destinatario@example.com'],
                fail_silently=False,
            )
            messages.success(request, 'Te has suscrito correctamente al boletín.')
            return redirect('home')
    messages.error(request, 'Hubo un error al suscribirte al boletín. Por favor, intenta de nuevo.')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'core/register.html', {'form': form})

def profile_view(request):
    return render(request, 'core/profile.html')

def estanley_esmeril(request):
    product = get_object_or_404(Producto, nombre="STANLEY ESMERIL ANGULAR 4 1/2")
    return render(request, 'core/estanley_esmeril.html', {'product': product})

def estanley_sierra(request):
    product = get_object_or_404(Producto, nombre="STANLEY SIERRA")
    return render(request, 'core/estanley_sierra.html', {'product': product})

def soldadora_indurarc(request):
    product = get_object_or_404(Producto, nombre="SOLDADORA INDURARC")
    return render(request, 'core/soldadora_indurarc.html', {'product': product})

def volcanita(request):
    product = get_object_or_404(Producto, nombre="VOLCANITA")
    return render(request, 'core/volcanita.html', {'product': product})

def teja(request):
    product = get_object_or_404(Producto, nombre="TEJA")
    return render(request, 'core/teja.html', {'product': product})

def volcan_rollo_lana(request):
    product = get_object_or_404(Producto, nombre="VOLCAN ROLLO LANA")
    return render(request, 'core/volcan_rollo_lana.html', {'product': product})

def volcan_huincha(request):
    product = get_object_or_404(Producto, nombre="VOLCAN HUINCHA")
    return render(request, 'core/volcan_huincha.html', {'product': product})

def cadena(request):
    product = get_object_or_404(Producto, nombre="CADENA")
    return render(request, 'core/cadena.html', {'product': product})

def inchalam_malla(request):
    product = get_object_or_404(Producto, nombre="INCHALAM MALLA")
    return render(request, 'core/inchalam_malla.html', {'product': product})

def materiales_view(request):
    productos = Producto.objects.filter(categoria='materiales').order_by('nombre')
    return render(request, 'core/materiales.html', {'productos': productos})

def ladrillo(request):
    product = get_object_or_404(Producto, nombre="LADRILLO")
    return render(request, 'core/ladrillo.html', {'product': product})

def mortero(request):
    product = get_object_or_404(Producto, nombre="MORTERO")
    return render(request, 'core/mortero.html', {'product': product})

def fierro_hormigon(request):
    product = get_object_or_404(Producto, nombre="FIERRO HORMIGON")
    return render(request, 'core/fierro_hormigon.html', {'product': product})

def silicona(request):
    product = get_object_or_404(Producto, nombre="SILICONA")
    return render(request, 'core/silicona.html', {'product': product})

def rodillo(request):
    product = get_object_or_404(Producto, nombre="RODILLO")
    return render(request, 'core/rodillo.html', {'product': product})

def pasta_muro(request):
    product = get_object_or_404(Producto, nombre="PASTA MURO")
    return render(request, 'core/pasta_muro.html', {'product': product})

def electricos(request):
    productos = Producto.objects.filter(categoria='electricos').order_by('nombre')
    return render(request, 'core/electricos.html', {'productos': productos})

def bateria_ion(request):
    product = get_object_or_404(Producto, nombre="BATERIA ION")
    return render(request, 'core/bateria_ion.html', {'product': product})

def compresor_ack_24(request):
    product = get_object_or_404(Producto, nombre="COMPRESOR ACK 24")
    return render(request, 'core/compresor_ack_24.html', {'product': product})

def compresor_ack(request):
    product = get_object_or_404(Producto, nombre="COMPRESOR ACK")
    return render(request, 'core/compresor_ack.html', {'product': product})

def hidrolavadora_k3(request):
    product = get_object_or_404(Producto, nombre="HIDROLAVADORA K3")
    return render(request, 'core/hidrolavadora_k3.html', {'product': product})

def placa_compactadora(request):
    product = get_object_or_404(Producto, nombre="PLACA COMPACTADORA")
    return render(request, 'core/placa_compactadora.html', {'product': product})

def soldadora_dw(request):
    product = get_object_or_404(Producto, nombre="SOLDADORA DW")
    return render(request, 'core/soldadora_dw.html', {'product': product})

def herramientas(request):
    productos = Producto.objects.filter(categoria='herramientas').order_by('nombre')
    return render(request, 'core/herramientas.html', {'productos': productos})

def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'core/producto_detalle.html', {'producto': producto})

def bodeguero_view(request):
    return render(request, 'core/bodeguero.html')

def contador_view(request):
    return render(request, 'core/contador.html')
