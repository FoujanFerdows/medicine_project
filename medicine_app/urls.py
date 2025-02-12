from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),  
]

