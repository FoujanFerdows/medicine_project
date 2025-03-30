from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),  
]
urlpatterns = [
    path('about/', views.about, name='about'),  # Add About Us page route
]
