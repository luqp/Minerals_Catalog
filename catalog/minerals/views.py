import random

from django.db import connection
from django.forms.models import model_to_dict
from django.shortcuts import render, get_object_or_404

from minerals.models import Mineral


def obtain_order_fields(star):
    '''
        Selects all name field from mineral Model 
        and order them in descendent way to be returned in a list
    '''
    fields = []
    query = 'SELECT COUNT("{}") FROM minerals_Mineral '
    query += 'WHERE "{}" <>""'
    with connection.cursor() as cursor:
        for field in Mineral._meta.get_fields()[star:]:
            count = cursor.execute(
                    query.format(field.name, field.name)
                ).fetchone()[0]
            count_field = (count, field.name)
            fields.append(count_field)

    fields.sort(reverse = True)
    return [field for _, field in fields]


def index(request):
    ''' 
        Render a page with the name of each mineral in the database
    '''
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    '''
        Converts mineral model's attributes in a list
        and render them
    '''
    mineral_model = get_object_or_404(Mineral, pk=pk)
    names_fields = obtain_order_fields(4)
    dict_fields = model_to_dict(mineral_model)
    mineral_fields = [(key, dict_fields[key]) for key in names_fields]

    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral_model,
                   'mineral_fields': mineral_fields})
