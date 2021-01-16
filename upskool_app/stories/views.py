from django.shortcuts import render,  redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Story view

class StoryListView(ListView):
    model = Stories
    template_name = 'stories/stories.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'stories'
    ordering = ['-story_date_posted']
    paginate_by = 5

class UserStoryListView(ListView):
    model = Stories
    template_name = 'stories/user_stories.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'stories'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Stories.objects.filter(story_author=user).order_by('-story_date_posted')


class StoryDetailView(DetailView):
    model = Stories


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Stories
    fields = ['story_title', 'story_content']

    def form_valid(self, form):
        form.instance.story_author = self.request.user
        return super().form_valid(form)


class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Stories
    fields = ['story_title', 'story_content']

    def form_valid(self, form):
        form.instance.story_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        st = self.get_object()
        if self.request.user == st.story_author:
            return True
        return False

class StoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Stories
    success_url = '/'

    def test_func(self):
        st = self.get_object()
        if self.request.user == st.story_author:
            return True
        return False


