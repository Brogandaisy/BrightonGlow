from django import template
from decimal import Decimal, InvalidOperation

register = template.Library()


@register.filter
def calculate_points(price):
    try:
        price = Decimal(price)
        return int(price) // 10
    except (InvalidOperation, ValueError, TypeError):
        return 0
