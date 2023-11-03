from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Car

def home(request):
    cars = Car.objects.all()
    return render(request, 'home/site/src/index.html', {'cars': cars})
