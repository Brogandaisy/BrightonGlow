from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    """Inline display for order items in the admin panel."""
    model = OrderItem
    extra = 1  

class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for managing orders."""
    list_display = ('id', 'user', 'email', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'status')
    inlines = [OrderItemInline]

    list_editable = ('status',) 

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
