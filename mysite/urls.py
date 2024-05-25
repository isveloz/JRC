# mysite/urls.py o jrc/urls.py

from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
