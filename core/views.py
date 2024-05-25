import locale
from django.core.paginator import Paginator # type: ignore
from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore
from .models import Producto

# Configurar la localización para CLP
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

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
    return render(request, 'core/contacto.html')

# Vistas para productos específicos
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

def pasta_muro(request):
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
