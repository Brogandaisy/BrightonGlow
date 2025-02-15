from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from bag.bag import Bag

def home(request):
    return render(request, 'products/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_to_bag(request, product_id):
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.add(product=product)
    request.session['total'] = bag.get_total_price()  
    return redirect('bag_detail')

def bag_detail(request):
    bag = Bag(request)
    total = bag.get_total_price()
    request.session['total'] = total
    return render(request, 'bag/bag_detail.html', {'bag': bag, 'total': total})