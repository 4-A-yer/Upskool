from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('ngo_register/', views.ngoregister, name='ngo-register'),
    path('ngo_profile/',views.ngoprofile, name='ngo-profile'),
    path('ngo-login/', auth_views.LoginView.as_view(template_name='ngo/login.html'), name='ngo-login'),
    path('ngo-logout/', auth_views.LogoutView.as_view(template_name='ngo/logout.html'), name='ngo-logout'),
]
