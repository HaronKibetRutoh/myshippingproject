from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    template = 'contact/contact.html'
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Thank you for your message. We will respond as soon as possible')
            return redirect('quote:success')
    else:
        form = ContactForm
    context = {'form': form,}
    return render(request, template, context)
