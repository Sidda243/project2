from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Strings(request):
    return HttpResponse('This is a first string')

def Strings1(request):
    return HttpResponse('We are in the django class')

def Strings2(request):
    return HttpResponse('The monday session of django is going well')