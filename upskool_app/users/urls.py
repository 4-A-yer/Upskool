from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    ReqListView,
    ReqDetailView,
    ReqCreateView,
    ReqUpdateView,
    ReqDeleteView
)


urlpatterns = [
    path('register/', views.register, name='upskool-register'),
    path('', views.home, name='upskool-home'),
    path('profile/',views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('requirements/',ReqListView.as_view(), name='requirements'),
    path('stories/', views.stories, name='stories'),
    path('requirements/<int:pk>/',ReqDetailView.as_view() , name='req-detail'),
    path('requirements/new/', ReqCreateView.as_view(), name='req-create'),
    path('requirements/<int:pk>/update/', ReqUpdateView.as_view(), name='req-update'),
    path('requirements/<int:pk>/delete/', ReqDeleteView.as_view(), name='req-delete'),
]

