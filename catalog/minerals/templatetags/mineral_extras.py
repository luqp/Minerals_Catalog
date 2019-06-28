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
    return random.randint(1, size) if size else 0


@register.simple_tag
def minerals_groups(param):
    q_groups = Mineral.objects.values(param).distinct()
    groups = [key[param] for key in list(q_groups)]
    groups.sort()
    return groups

@register.simple_tag
def minerals_colors():
    colors_names = {
        'beige':                '#F5F5DC',
        'black':                '#000000',
        'blue':                 '#0000FF',
        'brown':                '#A52A2A',
        'cyan':                 '#00FFFF',
        'gold':                 '#FFD700',
        'gray':                 '#808080',
        'green':                '#008000',
        'indigo':               '#4B0082',
        'ivory':                '#FFFFF0',
        'lavender':             '#E6E6FA',
        'magenta':              '#FF00FF',
        'navy':                 '#000080',
        'olive':                '#808000',
        'orange':               '#FFA500',
        'pink':                 '#FFC0CB',
        'purple':               '#800080',
        'red':                  '#FF0000',
        'salmon':               '#FA8072',
        'silver':               '#C0C0C0',
        'snow':                 '#FFFAFA',
        'violet':               '#EE82EE',
        'white':                '#FFFFFF',
        'yellow':               '#FFFF00',
    }
    return colors_names.keys()

