from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'full_name', 'email', 'phone', 'skin_type', 'created_at'
    )
    list_filter = ('skin_type', 'address_country', 'created_at')
    search_fields = ('user__username', 'email', 'full_name', 'phone')
