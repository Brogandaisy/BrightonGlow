# payments/views.py (Django)
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    total = request.session.get('total', 0)  

    if not isinstance(total, (int, float)) or total <= 0:
        return redirect('payment_error')  
    
    try:
        order = Order.objects.create(
            user=request.user,
            total_price=total,
            status='PENDING'
        )

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {'name': f'Order {order.id}'},
                    'unit_amount': int(total * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success')),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )

        order.stripe_payment_intent = session.id
        order.save()

        return redirect(session.url)
    except Exception as e:
        return render(request, 'payments/error.html', {'message': f'Error processing payment: {e}'})

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_cancel(request):
    return render(request, 'payments/cancel.html')

def payment_error(request):
    return render(request, 'payments/error.html', {'message': 'An error occured during checkout.'})
