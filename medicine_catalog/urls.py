from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),  # This includes the URLs from your 'catalog' app
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Add this to serve static files in development
