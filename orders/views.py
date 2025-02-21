from django.shortcuts import render, get_object_or_404
from products.models import Product
from .forms import CheckoutForm
from decimal import Decimal
from bag.bag import Bag

def checkout(request):
    """Checkout view - retrieves bag contents from session and attaches product names."""
    bag = request.session.get('bag', {})
    total = request.session.get('total', 0)

    bag_items = []
    for product_id, item in bag.items():
        product = get_object_or_404(Product, id=product_id) 
        bag_items.append({
            'id': product_id,
            'name': product.name,
            'quantity': item['quantity'],
            'price': Decimal(item['price']),
            'total_price': Decimal(item['price']) * item['quantity'],
        })

    form = CheckoutForm()

    return render(request, 'orders/checkout.html', {
        'bag': bag_items,
        'total': total,
        'form': form,  
    })