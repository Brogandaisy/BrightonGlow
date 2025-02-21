# brightonglow/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def checkout(request):
    return render(request, 'orders/checkout.html')

def checkout_view(request):
    return render(request, 'orders/checkout.html')


# Payment views in payments app
def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_cancel(request):
    return render(request, 'payments/payment_cancel.html')