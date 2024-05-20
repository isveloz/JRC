from django.core.paginator import Paginator # type: ignore
from django.shortcuts import render # type: ignore
from .models import Producto

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def productos(request):
    productos_list = Producto.objects.all().order_by('Nombre')  # Ordenar por nombre del producto
    paginator = Paginator(productos_list, 6)  # Mostrar 6 productos por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/productos.html', {'page_obj': page_obj})

def contacto(request):
    return render(request, 'core/contacto.html')
