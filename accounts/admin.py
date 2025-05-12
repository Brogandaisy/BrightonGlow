from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email',
                    'loyalty_points', 'skin_type')
    list_editable = ('loyalty_points',)
    search_fields = ('user__username', 'email', 'full_name')
