# brightonglow/views.py
from django.shortcuts import render
from products.models import Product


def home(request):
    featured_products = Product.objects.order_by('?')[:3]
    return render(request, 'home.html', {'featured_products': featured_products})

def checkout(request):
    return render(request, 'orders/checkout.html')

def checkout_view(request):
    return render(request, 'orders/checkout.html')


# Payment views in payments app
def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_cancel(request):
    return render(request, 'payments/payment_cancel.html')