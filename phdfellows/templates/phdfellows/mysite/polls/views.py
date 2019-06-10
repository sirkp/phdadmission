from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Polls Homepage')

def detail(request):
    return HttpResponse('Homepage')
