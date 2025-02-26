from django.contrib import admin
from django.urls import path, include
from orders import views as order_views
from bag import views as bag_views
from payments import views as payment_views
from . import views
from payments.views import webhook
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),  # Homepage
    path('admin/', admin.site.urls),  # Django admin
    path('accounts/', include('accounts.urls')),  # Include URLs 'accounts'
    path('products/', include('products.urls')),  # Include URLs for 'products'
    path('bag/', include('bag.urls')),  # Include URLs from the 'bag' app
    path('payments/', include('payments.urls')),  # Include URLs 'payments'
    path('orders/', include('orders.urls')),  # Include URLs 'orders' app
    path('payment-success/', payment_views.payment_success, name='payment_success'),  # Payment success page
    path('payment-cancel/', payment_views.payment_cancel, name='payment_cancel'),  # Payment cancellation page
    path('webhook/', webhook, name='stripe-webhook'),  # Stripe webhook
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)