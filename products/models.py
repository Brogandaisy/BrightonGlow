from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SkinType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    skin_types = models.ManyToManyField(SkinType, blank=True)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        result = self.reviews.aggregate(avg=Avg('rating'))['avg']
        return round(
            result, 1) if result else None  # return None if no reviews

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.product.name}"
