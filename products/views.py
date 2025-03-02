from django.shortcuts import render, get_object_or_404, redirect
from bag.bag import Bag
from .models import Product, Category

def products_home(request):
    skin_type_id = request.GET.get('skin_type')
    products = Product.objects.all()
    skin_types = SkinType.objects.all()

    if skin_type_id:
        products = products.filter(skin_type_id=skin_type_id)

    return render(request, "products/products_home.html", {
        "products": products,
        "skin_types": skin_types,
    })

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

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })