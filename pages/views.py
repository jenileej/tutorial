from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # what we want to happen
    return render(request, 'pages/index.html')

def about(request): 
    # render a template
    return render(request, 'pages/about.html')

