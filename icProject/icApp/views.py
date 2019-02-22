# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request, name):
    return render(request, 'icApp/index.html')
