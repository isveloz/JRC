from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('colaborador_login/', views.colaborador_login, name='colaborador_login'),
    path('cliente_login/', views.cliente_login, name='cliente_login'),
    path('bodeguero_login/', views.bodeguero_login, name='bodeguero_login'),
    path('contador_login/', views.contador_login, name='contador_login'),
    path('register/', views.register, name='register'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('producto/<int:producto_id>/', views.product_detail, name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('procesar_pago/', views.procesar_pago, name='procesar_pago'),
    path('transaccion_exitosa/', views.pago_exitoso, name='transaccion_exitosa'),
    path('tareas/', views.listar_tareas, name='listar_tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
