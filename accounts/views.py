from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


def signin(request):
    template = 'users/login.html'
    if request.method == 'POST':
        email = request.POST.get('email')
        password =  request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # messages.info(request, 'Login successful!')
            return redirect('quote:home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('users:signin')
    return render(request, template)


def register(request):
    template = 'users/register.html'
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            # phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('users:signin')
    else:
        form = CustomUserCreationForm
    context = {
        'form': form,
    }
    return render(request, template, context)

def logout_request(request):
    logout(request)
    return redirect("quote:home")
