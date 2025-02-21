import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from bag.bag import Bag
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_view(request):  
    """Handles checkout, creates Stripe session, and redirects to payment."""
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
            success_url=request.build_absolute_uri(reverse('order_confirmation', args=[order.id])),  # ✅ Redirect to confirmation
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )

        order.stripe_payment_intent = session.id
        order.save()

        return redirect(session.url) 

    except stripe.error.StripeError as e:
        return render(request, 'payments/error.html', {'message': f'Stripe error: {e}'})
    except Exception as e:
        return render(request, 'payments/error.html', {'message': f'Error processing payment: {e}'})

def order_confirmation(request, order_id):
    """Displays order confirmation page after successful payment."""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/confirmation.html', {'order': order})
