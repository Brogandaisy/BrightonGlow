# bag/views.py

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .bag import Bag

from django.http import JsonResponse
import json

def bag_add(request, product_id):
    """Adds a product to the shopping bag, updates session, and returns JSON response."""
    
    if request.method == "POST":
        bag = Bag(request)
        product = get_object_or_404(Product, id=product_id)

        # Get quantity from AJAX request
        try:
            data = json.loads(request.body)
            quantity = int(data.get("quantity", 1))  # Default to 1 if missing
        except (json.JSONDecodeError, ValueError):
            quantity = 1  # Fallback to 1 if there's an error
        
        bag.add(product=product, quantity=quantity)

        # Convert bag items to a format suitable for session storage
        session_bag = {
            str(k): {'quantity': v['quantity'], 'price': float(v['price'])}
            for k, v in bag.bag.items()
        }

        request.session['bag'] = session_bag
        request.session['total'] = float(bag.get_total_price())
        request.session.modified = True  # Ensure session updates are saved

        return JsonResponse({
            'message': f"{product.name} (x{quantity}) added to bag!",
            'total': request.session['total']
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)

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