from django.shortcuts import render, get_object_or_404, redirect
from bag.bag import Bag
from .models import SkinType, Product, Category, Review
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SkinQuizForm
from collections import Counter

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
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
    else:
        form = ReviewForm()

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })


def category_detail(request, category_name):
    """Displays products belonging to a specific category."""

    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)

    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })


@login_required
def edit_review(request, product_id, review_id):
    review = get_object_or_404(Review, id=review_id, product_id=product_id)

    if request.user != review.user:
        messages.error(request, "You can only edit your own reviews.")
        return redirect('product_detail', product_id=product_id)

    form = ReviewForm(request.POST or None, instance=review)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Review updated successfully.")
        return redirect('product_detail', product_id=product_id)

    return render(
        request, 'products/edit_review.html',
        {'form': form, 'product': review.product})


@login_required
def delete_review(request, product_id, review_id):
    review = get_object_or_404(Review, id=review_id, product_id=product_id)

    if request.user != review.user:
        messages.error(request, "You can only delete your own reviews.")
        return redirect('product_detail', product_id=product_id)

    if request.method == 'POST':
        review.delete()
        messages.success(request, "Review deleted successfully.")
        return redirect('product_detail', product_id=product_id)

    return render(
        request, 'products/delete_review.html', {'review': review})


def skin_quiz(request):
    if request.method == 'POST':
        form = SkinQuizForm(request.POST)
        if form.is_valid():
            answers = [
                form.cleaned_data['q1'],
                form.cleaned_data['q2'],
                form.cleaned_data['q3'],
            ]
            skin_type = Counter(answers).most_common(1)[0][0]
            return redirect(f'/products/?skin_type={skin_type}')
    else:
        form = SkinQuizForm()

    return render(request, 'products/skin_quiz.html', {'form': form})
