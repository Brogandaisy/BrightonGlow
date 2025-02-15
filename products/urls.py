from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/add/', views.add_to_bag, name='add_to_bag'),
    path('bag/', views.bag_detail, name='bag_detail'),
]
