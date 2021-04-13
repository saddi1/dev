from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="",
                           widget=forms.TextInput(attrs={'placeholder': 'Name*', 'class': "form-control p-4"}))
    email = forms.EmailField(required=True, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Email*', 'class': "form-control p-4"}))
    number = forms.CharField(required=True, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Number*', 'class': "form-control p-4"}))
    message = forms.CharField(required=True, label="", widget=forms.Textarea(attrs={'placeholder': 'Write Something '
                                                                                                   'here*'}))
