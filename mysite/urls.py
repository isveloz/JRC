# mysite/urls.py
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Incluye las rutas de la aplicación core
]
