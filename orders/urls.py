from django.urls import path
from . import views

urlpatterns = [
    path('confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
