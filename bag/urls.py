from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_detail, name='bag_detail'),
    path('add/<int:product_id>/', views.bag_add, name='bag_add'),
    path('adjust/<int:product_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<int:product_id>/', views.bag_remove, name='bag_remove'),
]