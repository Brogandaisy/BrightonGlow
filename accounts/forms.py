from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'email', 'address_line1', 'address_county', 'address_country', 'address_postcode']