from django.urls import path
from . import views
from .views import (
    StoryListView,
    StoryDetailView,
    StoryCreateView,
    StoryUpdateView,
    StoryDeleteView,
    UserStoryListView

)


urlpatterns = [

    path('user/<str:username>', UserStoryListView.as_view(), name='user_story'),
    path('story/',StoryListView.as_view(), name='story'),
    path('stories/<int:pk>/',StoryDetailView.as_view() , name='story-detail'),
    path('stories/new/', StoryCreateView.as_view(), name='story-create'),
    path('storiess/<int:pk>/update/', StoryUpdateView.as_view(), name='story-update'),
    path('stories/<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete'),
]

