# urls.py

from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Map the home view to the root URL
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),  # Map medicine detail view
]
