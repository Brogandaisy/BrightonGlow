import stripe
import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order, OrderItem
from bag.bag import Bag
from django.core.mail import send_mail


stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    total = float(request.session.get('total', 0))

    if not isinstance(total, (int, float)) or total <= 0:
        return redirect('payment_error')

    try:
        bag = Bag(request)
        user = request.user if request.user.is_authenticated else None
        email = request.user.email if request.user.is_authenticated else None
        order = Order.objects.create(user=user, email=email, total_price=total, status='PENDING')
        request.session['order_id'] = order.id

        line_items = []

        for item in bag:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price']
            )

            line_items.append({
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": int(100 * item['price']),
                    "product_data": {
                        "name": item["product"].name,  
                    },
                },
                "quantity": item["quantity"],
            })

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            currency="gbp",
            line_items=line_items,  
            metadata={'order_id': order.id},
            customer_email=email if email else None,
            shipping_address_collection={"allowed_countries": ["GB"]},
            shipping_options=[
                {
                    "shipping_rate_data": {
                        "display_name": "Standard Shipping, 2-3 Working Days",
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

        order.stripe_payment_intent = session.id
        order.save()

        return redirect(session.url, code=303)

    except Exception as e:
        print(f"Checkout Error: {str(e)}")
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
            order_id = session.get('metadata', {}).get('order_id')
            customer_details = session.get("customer_details", {})
            customer_email = customer_details.get("email")

            if order_id:
                try:
                    order = Order.objects.get(id=order_id)
                    order.status = "PAID"

                    if customer_email:
                        order.email = customer_email
                        order.save()

                    if "shipping_details" in session:
                        order.shipping_name = session["shipping_details"]["name"]
                        order.shipping_address = session["shipping_details"]["address"]["line1"]
                        order.shipping_city = session["shipping_details"]["address"]["city"]
                        order.shipping_postcode = session["shipping_details"]["address"]["postal_code"]
                        order.shipping_country = session["shipping_details"]["address"]["country"]

                    order.save()

                    order_items = OrderItem.objects.filter(order=order)
                    item_list = "\n".join([
                        f"{item.product.name} (x{item.quantity}) - £{item.price:.2f}"
                        for item in order_items
                    ])

                    send_mail(
                        'Your Order Confirmation - Brighton GLOW',
                        f"Hello,\n\nThank you for your order!\n\n"
                        f"Here are the details of your purchase:\n\n"
                        f"Order ID: {order.id}\n"
                        f"{item_list}\n\n"
                        f"Total: £{order.total_price:.2f}\n\n"
                        f"Your order is now being processed.\n"
                        f"Thank you for shopping with us at Brighton GLOW! ✨",
                        'brightonglowskincare@gmail.com',
                        [customer_email],
                        fail_silently=False,
                    )

                    print(f"✅ Order {order.id} updated to PAID, confirmation email sent.")

                except Order.DoesNotExist:
                    print('XXX Could not find the order')

        return JsonResponse({"status": "success"}, status=200)

    except ValueError:
        return JsonResponse({"error": "Invalid payload"}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({"error": "Invalid signature"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)




def payment_success(request):
    order_id = request.session.get('order_id')

    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            bag = Bag(request)
            bag.clear()
            del request.session['order_id']
            request.session.modified = True
            return render(request, 'payments/success.html', {'order': order})
        except Order.DoesNotExist:
            pass

    return render(request, 'payments/success.html')

def payment_cancel(request):
    order_id = request.session.get('order_id')
    print('✅✅✅HELLO')
    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            if order.status == 'PENDING':
                order.status == 'CANCELLED'
                order.save()
        except Order.DoesNotExist:
            pass
    return render(request, 'payments/cancel.html')

def payment_error(request):
    return render(request, 'payments/error.html', {'message': 'An error occurred during checkout.'})