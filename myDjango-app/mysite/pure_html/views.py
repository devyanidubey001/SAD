from django.shortcuts import render
from django.template import loader
# Create your views here.


def index (request): 
    return render(request, 'index.html')
def button (request):
    return render(request, 'button.html')
def button2 (request):
    return render(request, 'button2.html')
def interval (request):
    return render(request,'interval.html')
