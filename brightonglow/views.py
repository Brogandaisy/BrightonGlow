# brightonglow/views.py

from django.shortcuts import render
from products.models import Product

def home(request):
    """Displays the home page with randomly selected featured products."""
    featured_products = Product.objects.order_by('?')[:3]
    return render(request, 'home.html', {'featured_products': featured_products})

def checkout(request):
    """Renders the checkout page."""
    return render(request, 'orders/checkout.html')


def about(request):
    """Displays the about page with featured products."""
    featured_products = Product.objects.order_by('?')[:3]
    return render(request, 'about.html', {'featured_products': featured_products})

def contact(request):
    """Renders the contact page."""
    return render(request, 'contact.html')

def custom_404_view(request, exception):
    """Handles 404 errors with a custom page."""
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

def payment_success(request):
    """Displays the payment success page."""
    return render(request, 'payments/payment_success.html')

def payment_cancel(request):
    """Displays the payment cancel page."""
    return render(request, 'payments/payment_cancel.html')

def privacy_policy(request):
    """Render the Privacy Policy page."""
    return render(request, "privacy_policy.html")

