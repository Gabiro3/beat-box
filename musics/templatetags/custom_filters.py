from django import template
import datetime

register = template.Library()

@register.filter
def format_duration(value):
    if isinstance(value, datetime.timedelta):
        total_seconds = int(value.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        return f"{minutes}:{seconds:02d}"
    return value