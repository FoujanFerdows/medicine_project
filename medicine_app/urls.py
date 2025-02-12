from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'), 
]
