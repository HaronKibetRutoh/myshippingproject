from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-input'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact-input'}), required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'message'}), required=True)
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message',]