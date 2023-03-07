from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sangeetha(request):
    return HttpResponse('<h1> my name is sangeetha</h1>')
    
