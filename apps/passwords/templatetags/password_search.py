from django import template
from django.contrib.admin.views.main import SEARCH_VAR


register = template.Library()


@register.inclusion_tag('admin/passwords/password/search_form.html')
def search_form(cl):
    """
    Displays a search form for searching the list.
    """
    return {
        'cl': cl,
        'show_result_count': cl.result_count != cl.full_result_count,
        'search_var': SEARCH_VAR
    }
