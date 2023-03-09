from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pspk(request):
    return HttpResponse('<h1>man with golden heart</h1>')
def harish(request):
    return HttpResponse('<h1>good evening</h1>')
    