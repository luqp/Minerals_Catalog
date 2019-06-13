import json

from django.shortcuts import render
from django.db.utils import OperationalError


def index(request):
    return render(request, 'home.html')