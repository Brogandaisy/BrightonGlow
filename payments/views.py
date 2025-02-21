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
    total = float(request.session.get('total', 0))

    if not isinstance(total, (int, float)) or total <= 0:
        return redirect('payment_error')

    try:
        bag = Bag(request)

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
            mode='payment',
            currency="gbp",
            line_items=[
                {
                    "price_data": {
                        "currency": "gbp",
                        "unit_amount": int(100 * total),
                        "product_data": {
                            "name": "Your Order",
                            "description": "Physical product requiring shipping"
                        },
                    },
                    "quantity": 1,
                }
            ],
            shipping_address_collection={"allowed_countries": ["GB"]},
            shipping_options=[
                {
                    "shipping_rate_data": {
                        "display_name": "Standard Shipping",
                        "type": "fixed_amount",
                        "fixed_amount": {
                            "amount": 300,
                            "currency": "gbp"
                        }
                    }
                }
            ],
            success_url=request.build_absolute_uri(reverse('payment_success')),
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
)


        print("Stripe Session Data:", json.dumps(session, indent=4))

        order.stripe_payment_intent = session.id
        order.save()

        return redirect(session.url, code=303)

    except Exception as e:
        print(f"❌ Stripe Error: {str(e)}")
        return redirect('payment_error')


@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)

        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]
            order = Order.objects.filter(stripe_payment_intent=session.get("payment_intent")).first()

            if order:
                order.status = "PAID"
                if "shipping_details" in session:
                    order.shipping_name = session["shipping_details"]["name"]
                    order.shipping_address = session["shipping_details"]["address"]["line1"]
                    order.shipping_city = session["shipping_details"]["address"]["city"]
                    order.shipping_postcode = session["shipping_details"]["address"]["postal_code"]
                    order.shipping_country = session["shipping_details"]["address"]["country"]
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
