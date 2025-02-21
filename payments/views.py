import stripe
import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order, OrderItem
from bag.bag import Bag

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    total = request.session.get('total', 0)
    if not isinstance(total, (int, float)) or total <= 0:
        return redirect('payment_error')

    try:
        order = Order.objects.create(user=request.user, total_price=total, status='PENDING')
        for item in bag:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price']
            )
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=request.user.email if request.user.is_authenticated else None,  
            shipping_address_collection={  
                "allowed_countries": ["GB"],  
            },
            allow_promotion_codes=True,
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {'name': f'Order {order.id}'},
                    'unit_amount': int(total * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('order_confirmation', args=[order.id])),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )

        order.stripe_payment_intent = session.id
        order.save()
        bag.clear()

        return redirect(session.url)

    except stripe.error.StripeError as e:
        return render(request, 'payments/error.html', {'message': f'Stripe error: {e}'})
    except Exception as e:
        return render(request, 'payments/error.html', {'message': f'Error processing payment: {e}'})



@csrf_exempt
def webhook(request):
    """ Process Stripe webhook events """
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET  

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)

        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]
            order = Order.objects.filter(stripe_payment_intent=session["id"]).first()
            if order:
                order.status = "PAID"
                order.save()
                print(f"✅ Order {order.id} updated to PAID!")

        return JsonResponse({"status": "success"}, status=200)

    except ValueError:
        return JsonResponse({"error": "Invalid payload"}, status=400) 
    except stripe.error.SignatureVerificationError:
        return JsonResponse({"error": "Invalid signature"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_cancel(request):
    return render(request, 'payments/cancel.html')

def payment_error(request):
    return render(request, 'payments/error.html', {'message': 'An error occurred during checkout.'})
