"""
markdown filter
"""

from django import template
from django.utils.safestring import mark_safe
register = template.Library()

from markdown2 import markdown

@register.filter(name='md', is_safe=True)
def md(value, arg=None):
    try:
        if not arg:
            return mark_safe(markdown(value))
        else:
            mded =  markdown(value)
            rep = '<p class="%s">'%(arg)
            return mark_safe(mded.replace('<p>', rep))
    except Exception:
        return value