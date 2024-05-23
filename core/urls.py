from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('estanley-esmeril/', views.estanley_esmeril, name='estanley_esmeril'),
    path('estanley-sierra/', views.estanley_sierra, name='estanley_sierra'),
    path('soldadora-indurarc/', views.soldadora_indurarc, name='soldadora_indurarc'),
    path('volcanita/', views.volcanita, name='volcanita'),
    path('teja/', views.teja, name='teja'),
    path('volcan-rollo-lana/', views.volcan_rollo_lana, name='volcan_rollo_lana'),
    path('volcan-huincha/', views.volcan_huincha, name='volcan_huincha'),
    path('cadena/', views.cadena, name='cadena'),
    path('inchalam-malla/', views.inchalam_malla, name='inchalam_malla'),
    path('calcular_precio/', views.calcular_precio, name='calcular_precio'),
]
