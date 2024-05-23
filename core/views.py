import locale
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto

# Configurar la localización para CLP
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def productos(request):
    productos_list = Producto.objects.all().order_by('nombre')
    paginator_instance = Paginator(productos_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator_instance.get_page(page_number)
    return render(request, 'core/productos.html', {'page_obj': page_obj})

def contacto(request):
    return render(request, 'core/contacto.html')

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

def calcular_precio(request):
    cantidad = int(request.GET.get('cantidad', 1))
    precio_unitario = float(request.GET.get('precio_unitario', 0))
    total = cantidad * precio_unitario

    # Formatear el total en CLP
    total_clp = locale.format_string("%.0f", total, grouping=True)
    
    response_data = {'total': total_clp}
    return JsonResponse(response_data)
