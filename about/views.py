from django.shortcuts import render
from .models import AboutPage


def about_view(request):
    about = AboutPage.objects.first()
    return render(request, 'about/about.html', {'about': about})
