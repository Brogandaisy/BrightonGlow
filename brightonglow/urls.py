from django.contrib import admin
from django.urls import path, include, re_path
from payments import views as payment_views
from django.views.static import serve
from . import views
from payments.views import webhook
from django.conf.urls.static import static
from django.conf import settings
from .views import custom_404_view, custom_500_view
from about.views import about_page


urlpatterns = [
    path("", views.home, name="home"),  # Homepage
    path("admin/", admin.site.urls),  # Django admin
    path("accounts/", include("accounts.urls")),  # Include URLs 'accounts'
    path("products/", include("products.urls")),  # Include URLs for 'products'
    path("bag/", include("bag.urls")),  # Include URLs from the 'bag' app
    path("payments/", include("payments.urls")),  # Include URLs 'payments'
    path("orders/", include("orders.urls")),  # Include URLs 'orders' app
    path(
        "payment-success/",
        payment_views.payment_success,
        name="payment_success",
    ),  # Payment success page
    path(
        "payment-cancel/",
        payment_views.payment_cancel,
        name="payment_cancel",
    ),  # Payment cancellation page
    path(
        "payment-error/",
        payment_views.payment_error,
        name="payment_error",
    ),  # Payment error page
    path("webhook/", webhook, name="stripe-webhook"),  # Stripe webhook
    path("about/", about_page, name="about"),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    re_path(
        r"^sitemap\.xml$",
        serve,
        {"document_root": settings.BASE_DIR, "path": "sitemap.xml"},
    ),
    re_path(
        r"^robots\.txt$",
        serve,
        {"document_root": settings.BASE_DIR, "path": "robots.txt"},
    ),
    path('faqs/', include('faqs.urls')),
]

handler404 = custom_404_view
handler500 = custom_500_view

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
