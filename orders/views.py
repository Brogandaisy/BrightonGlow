from django.shortcuts import render, get_object_or_404
from orders.models import Order


def order_confirmation(request, order_id):
    """Displays order confirmation page after successful payment."""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/confirmation.html', {'order': order})
