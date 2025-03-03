# bag/views.py

import json
from decimal import Decimal
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
from .bag import Bag

def bag_add(request, product_id):
    """Adds a product to the shopping bag and updates the session data."""
    
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.add(product=product)

    # Convert bag items to a format suitable for session storage
    session_bag = {
        str(k): {'quantity': v['quantity'], 'price': float(v['price'])}
        for k, v in bag.bag.items()
    }

    request.session['bag'] = session_bag
    request.session['total'] = float(bag.get_total_price())
    request.session.modified = True  # Ensure session updates are saved

    # ✅ Add Django message for Bootstrap toast
    messages.success(request, f' {product.name} added to your bag!')

    # ✅ Redirect back to the **previous page (product page, category page, etc.)**
    # If no referer is found, default to the product page.
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect('product_detail', product_id=product.id)
    
@require_POST
def bag_remove(request, product_id):
    """Removes a product from the shopping bag and updates the session total."""
    
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.remove(product)

    request.session['total'] = bag.get_total_price()
    request.session.modified = True

    return redirect('bag_detail')

def bag_detail(request):
    """Displays the shopping bag contents along with the total price."""
    
    bag = Bag(request)
    total = float(bag.get_total_price())
    request.session['total'] = total

    # Ensure price values are stored as floats to avoid decimal issues
    for item in bag.bag.values():
        item['price'] = float(item['price'])
        item['total_price'] = float(item['price']) * item['quantity']

    request.session.modified = True

    return render(request, 'bag/bag_detail.html', {'bag': bag, 'total': total})

@require_POST
def adjust_bag(request, product_id):
    """Adjusts the quantity of a product in the shopping bag."""
    
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        bag.add(product=product, quantity=quantity, update_quantity=True)
    else:
        bag.remove(product)

    request.session['total'] = bag.get_total_price()
    request.session.modified = True

    return redirect('bag_detail')
