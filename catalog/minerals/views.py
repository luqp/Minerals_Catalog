import random

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.db.models import Q, Count

from minerals.models import Mineral


def fields_dataBase(db, star):
    '''
        Get fields from a database as a list
    '''
    fields = []
    for field in db._meta.get_fields()[star:]:
        count = db.objects.aggregate(
            field=Count(field.name, only=Q(field.name != "")))
        count_field = (count['field'], field.name)
        fields.append(count_field)
    fields.sort(reverse=True)
    return [field for _, field in fields]


names_fields = fields_dataBase(Mineral, 4)


def index(request):
    ''' 
        Render a page with the name of each mineral in the database
    '''
    minerals = Mineral.objects.all()
    return HttpResponseRedirect(reverse('minerals:search', kwargs={
        'term': 'A'
    }))


def mineral_detail(request, pk):
    '''
        Converts mineral model's attributes in a list
        and render them
    '''
    try:
        mineral_model = Mineral.objects.values().get(pk=pk)
    except Mineral.DoesNotExist:
        raise Http404
    fields = [(key, mineral_model[key]) for key in names_fields]
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral_model,
                   'mineral_fields': fields})


def search(request, term):
    if len(term) == 1:
        minerals = Mineral.objects.filter(name__istartswith=term)
    else:
        minerals = Mineral.objects.filter(group__icontains=term)
        if not len(minerals):
            minerals = Mineral.objects.filter(color__icontains=term)
    return render(request, 'minerals/index.html', {
        'minerals': minerals,
        'term': term,
    })


def search_in_all(request, term):
    '''
        Search in all fields of the database
    '''
    term = request.GET.get('q')
    list_queries = [Q(**{field + "__icontains": term})
                    for field in names_fields]
    queries = Q(name__icontains=term)|Q(image_caption__icontains=term)
    for query in list_queries:
        queries = queries | query
    minerals = Mineral.objects.filter(queries)
    return render(request, 'minerals/index.html', {
        'minerals': minerals,
    })
