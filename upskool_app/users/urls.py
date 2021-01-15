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
    # StoryListView,
    # StoryDetailView,
    # StoryCreateView,
    # StoryUpdateView,
    # StoryDeleteView,
    # UserStoryListView

)




urlpatterns = [
    path('register/', views.register, name='upskool-register'),
    path('', views.home, name='upskool-home'),
    path('user/<str:username>', UserReqListView.as_view(), name='user_requirement'),
    path('profile/<int:pk>',views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('requirements/',ReqListView.as_view(), name='requirements'),
    path('requirements/<int:pk>/',ReqDetailView.as_view() , name='req-detail'),
    path('requirements/new/', ReqCreateView.as_view(), name='req-create'),
    path('requirements/<int:pk>/update/', ReqUpdateView.as_view(), name='req-update'),
    path('requirements/<int:pk>/delete/', ReqDeleteView.as_view(), name='req-delete'),


    # path('user/<str:username>', UserStoryListView.as_view(), name='user_story'),
    # path('story/',StoryListView.as_view(), name='story'),
    # path('stories/<int:pk>/',StoryDetailView.as_view() , name='story-detail'),
    # path('stories/new/', StoryCreateView.as_view(), name='story-create'),
    # path('storiess/<int:pk>/update/', StoryUpdateView.as_view(), name='story-update'),
    # path('stories/<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete'),



]

