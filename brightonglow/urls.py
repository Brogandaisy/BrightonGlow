from django.contrib import admin
from django.urls import path, include
from orders import views as order_views
from bag import views as bag_views
from payments import views as payment_views
from payments.views import webhook
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('products.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('payments/', include('payments.urls')),
    path('checkout/', order_views.checkout, name='checkout'),
    path('payment-success/', payment_views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    path('webhook/', webhook, name='stripe-webhook'),
]
