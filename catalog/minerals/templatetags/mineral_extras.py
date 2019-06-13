from django import template
from django.utils.safestring import mark_safe

import markdown2
import random

from minerals.models import Mineral

register = template.Library()


@register.filter('replace_for_spaces')
def replace_for_spaces(value, arg):
    ''' Chages arg value for spaces '''
    return value.replace(arg, ' ')


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    ''' Coverts markdown text to HTML '''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)


@register.simple_tag
def random_number():
    try:
        size = Mineral.objects.all().count()
    except:
        size = 0
    return random.randint(1, size + 1) if size else 0
