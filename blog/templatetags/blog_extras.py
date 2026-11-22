from django import template
from django.conf import settings

register = template.Library()

@register.filter
def rating_label(value):
    if value in (None, ""):
        return "Без рейтинга"
    try:
        val = int(value)
    except (ValueError, TypeError):
        return "Без рейтинга"
        
    return settings.RATING_LABELS.get(val, "Без рейтинга")

@register.simple_tag
def plural_ru(value, one, few, many):
    try:
        n = abs(int(value))
    except (ValueError, TypeError):
        return f"{value} {many}"

    if 11 <= n % 100 <= 14:
        return f"{value} {many}"
    if n % 10 == 1:
        return f"{value} {one}"
    if 2 <= n % 10 <= 4:
        return f"{value} {few}"
    return f"{value} {many}"
