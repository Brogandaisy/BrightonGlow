from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form with an email field."""
    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerProfileForm(forms.ModelForm):
    """Form for updating customer profile details."""
    
    class Meta:
        model = Customer
        fields = [
            'phone', 'email', 'address_line1',
            'address_county', 'address_country', 'address_postcode'
        ]
