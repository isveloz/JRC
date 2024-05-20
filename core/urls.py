# core/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
]
