from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    ReqListView,
    ReqDetailView,
    ReqCreateView,
    ReqUpdateView,
    ReqDeleteView,
    UserReqListView

)


urlpatterns = [
    path('choice/', views.choice, name='choice'),
    path('choice-login/', views.choicelogin, name='choice-login'),
    path('register/', views.register, name='upskool-register'),
    path('', views.home, name='upskool-home'),
    path('user/<str:username>', UserReqListView.as_view(), name='user_requirement'),
    path('profile/',views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('requirements/',ReqListView.as_view(), name='requirements'),
    path('stories/', views.stories, name='stories'),
    path('requirements/<int:pk>/',ReqDetailView.as_view() , name='req-detail'),
    path('requirements/new/', ReqCreateView.as_view(), name='req-create'),
    path('requirements/<int:pk>/update/', ReqUpdateView.as_view(), name='req-update'),
    path('requirements/<int:pk>/delete/', ReqDeleteView.as_view(), name='req-delete'),
]

