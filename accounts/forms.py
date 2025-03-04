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
    SKIN_TYPES = [
        ('Oily', 'Oily'),
        ('Dry', 'Dry'),
        ('Combination', 'Combination'),
        ('Sensitive', 'Sensitive'),
        ('Normal', 'Normal'),
    ]

    skin_type = forms.ChoiceField(
        choices=SKIN_TYPES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Customer
        fields = ['full_name', 'phone', 'email', 'address_line1',
                  'address_county', 'address_country', 'address_postcode',
                  'skin_type']
