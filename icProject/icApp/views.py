# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Computer


# Create your views here.
def index(request, name):
    comp = get_object_or_404(Computer, name=name)
    return render(request, 'icApp/index.html', {'name': comp.name})


def details(request, name):
    return render(request, 'icApp/details.html')
