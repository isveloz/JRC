from django.urls import path # type: ignore
from .views import (
    home, about, productos, contacto, estanley_esmeril, estanley_sierra,
    soldadora_indurarc, volcanita, teja, volcan_rollo_lana, volcan_huincha,
    cadena, inchalam_malla, materiales_view, calcular_precio, ladrillo,
    mortero, fierro_hormigon, silicona, rodillo, pasta_muro
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('productos/', productos, name='productos'),
    path('contacto/', contacto, name='contacto'),
    path('estanley_esmeril/', estanley_esmeril, name='estanley_esmeril'),
    path('estanley_sierra/', estanley_sierra, name='estanley_sierra'),
    path('soldadora_indurarc/', soldadora_indurarc, name='soldadora_indurarc'),
    path('volcanita/', volcanita, name='volcanita'),
    path('teja/', teja, name='teja'),
    path('volcan_rollo_lana/', volcan_rollo_lana, name='volcan_rollo_lana'),
    path('volcan_huincha/', volcan_huincha, name='volcan_huincha'),
    path('cadena/', cadena, name='cadena'),
    path('inchalam_malla/', inchalam_malla, name='inchalam_malla'),
    path('materiales/', materiales_view, name='materiales'),
    path('calcular_precio/', calcular_precio, name='calcular_precio'),
    path('ladrillo/', ladrillo, name='ladrillo'),
    path('mortero/', mortero, name='mortero'),
    path('fierro_hormigon/', fierro_hormigon, name='fierro_hormigon'),
    path('silicona/', silicona, name='silicona'),
    path('rodillo/', rodillo, name='rodillo'),
    path('pasta_muro/', pasta_muro, name='pasta_muro'),
    path('herramientas/', pasta_muro, name='herramientas'),
    path('electricos/', pasta_muro, name='electricos'),
]
