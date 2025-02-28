# bag/views.py (Add Logging to Find Decimal Issue)
import json
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .bag import Bag
from decimal import Decimal

def bag_add(request, product_id):
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.add(product=product)

    session_bag = {str(k): {'quantity': v['quantity'], 'price': float(v['price'])} for k, v in bag.bag.items()}

    request.session['bag'] = session_bag
    request.session['total'] = float(bag.get_total_price())
    request.session.modified = True

    return redirect('bag_detail')

@require_POST
def bag_remove(request, product_id):
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.remove(product)
    request.session['total'] = bag.get_total_price()
    return redirect('bag_detail')


def bag_detail(request):
    bag = Bag(request)

    total = float(bag.get_total_price())
    request.session['total'] = total

    for item in bag.bag.values():
        item['price'] = float(item['price'])
        item['total_price'] = float(item['price']) * item['quantity']

    request.session.modified = True

    return render(request, 'bag/bag_detail.html', {'bag': bag, 'total': total})

@require_POST
def adjust_bag(request, product_id):
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        bag.add(product=product, quantity=quantity, update_quantity=True)
    else:
        bag.remove(product)

    request.session['total'] = bag.get_total_price()
    return redirect('bag_detail')
