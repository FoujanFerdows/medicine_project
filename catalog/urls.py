from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This maps to your home view
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),  # This maps to the medicine detail view
]
