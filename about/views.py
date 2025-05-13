from django.shortcuts import render
from .models import AboutPage
from products.models import Product


def about_view(request):
    about = AboutPage.objects.first()
    featured_products = Product.objects.order_by('?')[:3]
    return render(request, 'about/about.html', {
        'about': about,
        'featured_products': featured_products,
    })
