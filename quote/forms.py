from django import forms
from .models import Quote, Shopping

class QuoteForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'input'}))
    luggage_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What do you want shipped?', 'class': 'input'}))
    luggage_weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter weight of your cargo', 'class': 'input'}))
    luggage_dimensions = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter dimensions of your cargo', 'class': 'input'}))
    origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Which city are you shipping from?', 'class': 'input'}))
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Which city are you shipping to?', 'class': 'input'}))
    mode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter shipping mode', 'class': 'input'}))
    class Meta:
        model = Quote
        fields = ['name', 'email', 'phone', 'luggage_type', 'luggage_weight', 'luggage_dimensions', 'origin', 'destination', 'mode']


class ShoppingForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-input'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact-input'}), required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'message'}), required=True)
    class Meta:
        model = Shopping
        fields = ['name', 'email', 'phone', 'description']