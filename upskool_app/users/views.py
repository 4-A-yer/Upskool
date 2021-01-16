  
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
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
    
# Requirement views

class ReqListView(ListView):
    model = Requirement
    template_name = 'users/requirements.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'requirements'
    ordering = ['-date_posted']
    paginate_by = 5

class UserReqListView(ListView):
    model = Requirement
    template_name = 'users/user_requirement.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'requirements'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Requirement.objects.filter(author=user).order_by('-date_posted')


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


# register view

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


# profile View

@login_required
def profile(request, pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    cr_user = Profile.objects.get(pk=pk)

    result = False

    if cr_user.type == 'Gov':
        result = True

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'result': result,
        'cr_user': cr_user
    }

    return render(request, 'users/profile.html', context)




