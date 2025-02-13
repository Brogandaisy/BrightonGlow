from django.contrib import admin
from .models import Customer

admin.site.register(Customer)  # ✅ Allow managing customers in Django Admin
