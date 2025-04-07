from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),
    path('add_to_shopping_list/<int:medicine_id>/', views.add_to_shopping_list, name='add_to_shopping_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  
]
