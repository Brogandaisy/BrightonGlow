from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .bag import Bag

def bag_add(request, product_id):
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.add(product=product)
    return redirect('bag_detail')

def bag_remove(request, product_id):
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.remove(product)
    return redirect('bag_detail')

def bag_detail(request):
    bag = Bag(request)
    return render(request, 'bag/bag_detail.html', {'bag': bag})