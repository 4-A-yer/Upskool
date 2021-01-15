from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NgoRegisterForm, NgoUpdateForm, NgoProfileUpdateForm
from .models import *

# Create your views here.

def ngoregister(request):
    if request.method == 'POST':
        form = NgoRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('ngo-login')
    else:
        form = NgoRegisterForm()
    return render(request, 'ngo/register.html', {'form': form})

@login_required
def ngoprofile(request):
    if request.method == 'POST':
        u_form = NgoUpdateForm(request.POST, instance=request.ngouser)
        p_form = NgoProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.ngouser.ngoprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('ngo-profile')

    else:
        u_form = NgoUpdateForm(instance=request.ngouser)
        p_form = NgoProfileUpdateForm(instance=request.ngouser.ngoprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'ngo/profile.html', context)