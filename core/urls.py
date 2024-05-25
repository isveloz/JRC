# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Correct inclusion of admin URLs without namespace argument
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
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
    path('calcular_precio/', views.calcular_precio, name='calcular_precio'),
    path('bateria_ion/', views.bateria_ion, name='bateria_ion'),
    path('compresor_ack_24/', views.compresor_ack_24, name='compresor_ack_24'),
    path('compresor_ack/', views.compresor_ack, name='compresor_ack'),
    path('hidrolavadora_k3/', views.hidrolavadora_k3, name='hidrolavadora_k3'),
    path('placa_compactadora/', views.placa_compactadora, name='placa_compactadora'),
    path('soldadora_dw/', views.soldadora_dw, name='soldadora_dw'),
    path('herramientas/', views.herramientas, name='herramientas'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]
