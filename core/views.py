# views.py

from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.core.mail import send_mail # type: ignore
from django.core.paginator import Paginator # type: ignore
from django.http import JsonResponse # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
import locale
from .models import Producto, Cart, CartItem
from .forms import ContactoForm, RegistroForm
from .forms import AddToCartForm
from django.contrib.auth.decorators import login_required # type: ignore

# Configurar la localización para CLP
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            product = get_object_or_404(Producto, id=product_id)

            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.quantity += quantity
            cart_item.save()

            messages.success(request, f'Added {quantity} {product.nombre} to your cart.')
            return redirect('cart_view')
    return redirect('home')

@login_required
def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'core/cart.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('cart_view')

# Vista para la página de inicio
def home(request):
    return render(request, 'core/home.html')

# Vista para la página "Acerca de"
def about(request):
    return render(request, 'core/about.html')

# Vista para mostrar una lista paginada de productos
def productos(request):
    productos_list = Producto.objects.all().order_by('nombre')
    paginator_instance = Paginator(productos_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator_instance.get_page(page_number)
    return render(request, 'core/productos.html', {'page_obj': page_obj})

# Vista para la página de contacto
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
                'tu_correo@example.com',  # Cambia esto por tu correo
                ['destinatario@example.com'],  # Cambia esto por el destinatario
                fail_silently=False,
            )
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'core/contacto.html', {'form': form})

# Vista para manejar la sumisión del formulario de contacto
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
                'tu_correo@example.com',  # Cambia esto por tu correo
                ['destinatario@example.com'],  # Cambia esto por el destinatario
                fail_silently=False,
            )
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('contacto')
    messages.error(request, 'Hubo un error al enviar tu mensaje. Por favor, intenta de nuevo.')
    return redirect('contacto')

# Vista para manejar la sumisión del formulario de suscripción al boletín
def submit_newsletter_form(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        if correo:
            # Lógica para procesar la suscripción al boletín
            send_mail(
                'Suscripción al boletín',
                f"El correo {correo} se ha suscrito al boletín.",
                'tu_correo@example.com',  # Cambia esto por tu correo
                ['destinatario@example.com'],  # Cambia esto por el destinatario
                fail_silently=False,
            )
            messages.success(request, 'Te has suscrito correctamente al boletín.')
            return redirect('home')
    messages.error(request, 'Hubo un error al suscribirte al boletín. Por favor, intenta de nuevo.')
    return redirect('home')

# Vista para productos específicos
def estanley_esmeril(request):
    return render(request, 'core/estanley_esmeril.html')

def estanley_sierra(request):
    return render(request, 'core/estanley_sierra.html')

def soldadora_indurarc(request):
    return render(request, 'core/soldadora_indurarc.html')

def volcanita(request):
    return render(request, 'core/volcanita.html')

def teja(request):
    return render(request, 'core/teja.html')

def volcan_rollo_lana(request):
    return render(request, 'core/volcan_rollo_lana.html')

def volcan_huincha(request):
    return render(request, 'core/volcan_huincha.html')

def cadena(request):
    return render(request, 'core/cadena.html')

def inchalam_malla(request):
    return render(request, 'core/inchalam_malla.html')

# Vista para mostrar productos de la categoría "materiales"
def materiales_view(request):
    productos = Producto.objects.filter(categoria='materiales').order_by('nombre')
    return render(request, 'core/materiales.html', {'productos': productos})

# Vistas para productos específicos
def ladrillo(request):
    return render(request, 'core/ladrillo.html')

def mortero(request):
    return render(request, 'core/mortero.html')

def fierro_hormigon(request):
    return render(request, 'core/fierro_hormigon.html')

def silicona(request):
    return render(request, 'core/silicona.html')

def rodillo(request):
    return render(request, 'core/rodillo.html')

def pasta_muro(request):
    return render(request, 'core/pasta_muro.html')

def electricos(request):
    return render(request, 'core/electricos.html')

# Vista para calcular el precio total
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

# Vistas para productos específicos
def bateria_ion(request):
    return render(request, 'core/bateria_ion.html')

def compresor_ack_24(request):
    return render(request, 'core/compresor_ack_24.html')

def compresor_ack(request):
    return render(request, 'core/compresor_ack.html')

def hidrolavadora_k3(request):
    return render(request, 'core/hidrolavadora_k3.html')

def placa_compactadora(request):
    return render(request, 'core/placa_compactadora.html')

def soldadora_dw(request):
    return render(request, 'core/soldadora_dw.html')

def herramientas(request):
    return render(request, 'core/herramientas.html')

# Vista para la autenticación
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
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
