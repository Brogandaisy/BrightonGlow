from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import CheckoutForm
from cart.cart import Cart
from django.shortcuts import get_object_or_404


def checkout_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                status='PENDING',
                total_price=cart.get_total_price()
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            cart.clear()
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'cart': cart, 'form': form})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/confirmation.html', {'order': order})