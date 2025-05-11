from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    path('error/', views.payment_error, name='payment_error'),
    path('webhook/', csrf_exempt(views.webhook), name='stripe-webhook'),
]
