from django import template


register = template.Library()


@register.filter
def mask(password):
    return u'\u25CF' * len(password)
