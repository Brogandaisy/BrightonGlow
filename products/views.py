from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from bag.bag import Bag

def products_home(request):
    products = Product.objects.all()
    return render(request, 'products/products_home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_to_bag(request, product_id):
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1)) 

    bag.add(product=product, quantity=quantity)

    request.session['total'] = bag.get_total_price()
    return redirect('bag_detail')

def bag_detail(request):
    bag = Bag(request)
    total = bag.get_total_price()
    request.session['total'] = total
    return render(request, 'bag/bag_detail.html', {'bag': bag, 'total': total})