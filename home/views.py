from django.shortcuts import render

def home(request):
    return render(request, 'home/site/src/index.html')
