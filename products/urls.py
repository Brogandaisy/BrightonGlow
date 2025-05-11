from django.urls import path
from . import views

urlpatterns = [
    path(
        'products/', views.products_home, name='products_home'
    ),
    path(
        'products/<int:product_id>/',
        views.product_detail,
        name='product_detail',
    ),
    path(
        'products/<int:product_id>/add/',
        views.add_to_bag,
        name='add_to_bag',
    ),
    path(
        'category/<str:category_name>/',
        views.category_detail,
        name='category_detail',
    ),
    path(
        'bag/', views.bag_detail, name='bag_detail'
    ),
    path(
        'products/<int:product_id>/review/<int:review_id>/edit/',
        views.edit_review,
        name='edit_review'),
    path(
        'skin-quiz/',
        views.skin_quiz,
        name='skin_quiz'),
    path(
        'products/<int:product_id>/review/<int:review_id>/delete/',
        views.delete_review,
        name='delete_review'),
]
