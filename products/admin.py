from django.contrib import admin
from .models import Product, SkinType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('skin_types',)


admin.site.register(SkinType)
