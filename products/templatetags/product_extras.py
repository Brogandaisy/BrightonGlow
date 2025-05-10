from django import template

register = template.Library()


@register.filter
def calculate_points(price):
    try:
        return int(price) // 10
    except (ValueError, TypeError):
        return 0
