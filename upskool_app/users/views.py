  
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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


def home(request):
    return render(request, 'users/home.html')

class ReqListView(ListView):
    model = Requirement
    template_name = 'users/requirements.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'requirements'
    ordering = ['-date_posted']

class ReqDetailView(DetailView):
    model = Requirement

class ReqCreateView(LoginRequiredMixin, CreateView):
    model = Requirement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReqUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Requirement
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        req = self.get_object()
        if self.request.user == req.author:
            return True
        return False

class ReqDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Requirement
    success_url = '/'

    def test_func(self):
        req = self.get_object()
        if self.request.user == req.author:
            return True
        return False


def stories(request):
    return render(request, 'users/stories.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)