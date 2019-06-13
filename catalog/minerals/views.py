import random

from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict

from minerals.models import Mineral


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
    mineral_fields = list(
        model_to_dict(mineral_model).items()
    )[4:]
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral_model,
                   'mineral_fields': mineral_fields})
