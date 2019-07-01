import random

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.db.models import Q, Count

from minerals.models import Mineral


def get_popular_fields(request, db, start=4):
    '''
        Get the most popular fields from a database as a list
    '''
    if not request.session.get('popular_fields'):
        fields = []
        for field in db._meta.get_fields()[start:]:
            count = db.objects.aggregate(
                field=Count(field.name, only=Q(field.name != "")))
            count_field = (count['field'], field.name)
            fields.append(count_field)
        fields.sort(reverse=True)
        request.session['popular_fields'] = [field for _, field in fields]
    return request.session.get('popular_fields')


def index(request):
    ''' 
        Render a page with the name of each mineral in the database
    '''
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
    popular_fields = get_popular_fields(request, Mineral)
    fields = [(key, mineral_model[key]) for key in popular_fields]
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
    popular_fields = get_popular_fields(request, Mineral)
    list_queries = [Q(**{field + "__icontains": term})
                    for field in popular_fields]
    queries = Q(name__icontains=term)|Q(image_caption__icontains=term)
    for query in list_queries:
        queries = queries | query
    minerals = Mineral.objects.filter(queries)
    return render(request, 'minerals/index.html', {
        'minerals': minerals,
    })
