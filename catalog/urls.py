from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'), # Home view with search and letter filter
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine_detail'),
    path('add_to_medicine_list/<int:medicine_id>/', views.add_to_medicine_list, name='add_to_medicine_list'),
    path('remove_from_medicine_list/<int:medicine_id>/', views.remove_from_medicine_list, name='remove_from_medicine_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/password/', views.MyPasswordChangeView.as_view(),        name='password_change'),
]
