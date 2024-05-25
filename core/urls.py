from django.urls import path # type: ignore
from . import views
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
from django.contrib.auth import login, logout, authenticate # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('submit-contact/', views.submit_contact_form, name='submit_contact_form'),
    path('submit-newsletter/', views.submit_newsletter_form, name='submit_newsletter_form'),
    path('estanley_esmeril/', views.estanley_esmeril, name='estanley_esmeril'),
    path('estanley_sierra/', views.estanley_sierra, name='estanley_sierra'),
    path('soldadora_indurarc/', views.soldadora_indurarc, name='soldadora_indurarc'),
    path('volcanita/', views.volcanita, name='volcanita'),
    path('teja/', views.teja, name='teja'),
    path('volcan_rollo_lana/', views.volcan_rollo_lana, name='volcan_rollo_lana'),
    path('volcan_huincha/', views.volcan_huincha, name='volcan_huincha'),
    path('cadena/', views.cadena, name='cadena'),
    path('inchalam_malla/', views.inchalam_malla, name='inchalam_malla'),
    path('materiales/', views.materiales_view, name='materiales'),
    path('ladrillo/', views.ladrillo, name='ladrillo'),
    path('mortero/', views.mortero, name='mortero'),
    path('fierro_hormigon/', views.fierro_hormigon, name='fierro_hormigon'),
    path('silicona/', views.silicona, name='silicona'),
    path('rodillo/', views.rodillo, name='rodillo'),
    path('pasta_muro/', views.pasta_muro, name='pasta_muro'),
    path('electricos/', views.electricos, name='electricos'),
    path('bateria_ion/', views.bateria_ion, name='bateria_ion'),
    path('compresor_ack_24/', views.compresor_ack_24, name='compresor_ack_24'),
    path('compresor_ack/', views.compresor_ack, name='compresor_ack'),
    path('hidrolavadora_k3/', views.hidrolavadora_k3, name='hidrolavadora_k3'),
    path('placa_compactadora/', views.placa_compactadora, name='placa_compactadora'),
    path('soldadora_dw/', views.soldadora_dw, name='soldadora_dw'),
    path('calcular_precio/', views.calcular_precio, name='calcular_precio'),  # Añadir esta línea
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('herramientas/', views.herramientas, name='herramientas'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    path('producto/<int:producto_id>/', views.producto_detalle, name='producto_detalle'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
