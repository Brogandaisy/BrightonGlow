from django.shortcuts import render, get_object_or_404, redirect
from bag.bag import Bag
from .models import SkinType, Product, Category
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q


def products_home(request):
    """Enhanced search: Matches products by name,
    description, and handles multiple words."""

    skin_type_id = request.GET.get("skin_type")
    search_query = request.GET.get("search", "").strip()

    products = Product.objects.all()

    if skin_type_id:
        products = products.filter(skin_types__id=skin_type_id)

    # Initialise search_terms before using it
    search_terms = []
    if search_query:
        search_terms = search_query.split()

    if search_terms:
        search_filters = Q()
        for term in search_terms:
            search_filters |= (
                Q(name__icontains=term) |
                Q(description__icontains=term)
            )

        products = products.filter(search_filters)

    skin_types = SkinType.objects.all()

    return render(request, "products/products_home.html", {
        "products": products,
        "skin_types": skin_types,
        "search_query": search_query,
    })


def add_to_bag(request, product_id):
    """Adds a product to the shopping bag and updates total price."""

    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    bag.add(product=product, quantity=quantity)
    request.session['total'] = bag.get_total_price()

    return redirect('bag_detail')


def bag_detail(request):
    """Displays the shopping bag and total price."""

    bag = Bag(request)
    total = bag.get_total_price()
    request.session['total'] = total

    return render(request, 'bag/bag_detail.html', {'bag': bag, 'total': total})


def product_detail(request, product_id):
    """Displays details of a single product."""
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        """Product review form."""
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'products/product_detail.html', {
        'product': product,
        'form': form,
        'reviews': reviews,
    })


def category_detail(request, category_name):
    """Displays products belonging to a specific category."""

    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)

    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })
