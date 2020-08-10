from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import QuoteForm, ShoppingForm
from .models import Quote, Shopping


def home(request):
    template = 'quote/home.html'
    return render(request, template)

def about(request):
    template = 'quote/about.html'
    return render(request, template)


def success(request):
    template = 'quote/success.html'
    return render(request, template)

def shopping(request):
    template = 'quote/shopping.html'
    form = ShoppingForm
    if request.method == 'POST':
        form = ShoppingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']
            Shopping.objects.create(name=name, email=email, phone=phone, description=description)
            messages.success(request, 'We have received your shopping request!')
            return redirect('quote:success')
    else:
        form = ShoppingForm
        context = {
            'form': form,
        }        
    return render(request, template, context)

def quote(request):
    template = 'quote/quote.html'
    form = QuoteForm
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            luggage_type = form.cleaned_data['luggage_type']
            luggage_weight = form.cleaned_data['luggage_weight']
            luggage_dimensions = form.cleaned_data['luggage_dimensions']
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            mode = form.cleaned_data['mode']
            Quote.objects.create(name=name, email=email, phone=phone, luggage_type=luggage_type, luggage_weight=luggage_weight, luggage_dimensions=luggage_dimensions, origin=origin, destination=destination, mode=mode)
            messages.success(request, 'We have received your shipping assistance request!')
            return redirect('quote:success')
    else:
        form = QuoteForm
    context = {
        'form': form,
    }
    return render(request, template, context)







            
        