from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import CheckoutForm
bag.bag import Bag
from django.shortcuts import get_object_or_404


def checkout_view(request):
    bag = Bag(request)  # Use Bag instead of Cart
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                status='PENDING',
                total_price=bag.get_total_price()  # Changed cart to bag
            )
            for item in bag:  # Changed cart to bag
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            bag.clear()  # Changed cart.clear() to bag.clear()
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'bag': bag, 'form': form})  # Changed cart to bag


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/confirmation.html', {'order': order})