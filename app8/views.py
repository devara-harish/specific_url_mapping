from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def power_star(request):
    return HttpResponse('<marquee><h1>demigod</h1>')
def job(request):
    return HttpResponse('<marquee><h1>welcome to the project</h1>')
