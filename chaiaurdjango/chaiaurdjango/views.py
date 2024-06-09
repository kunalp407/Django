from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, world. You are at chai or django")
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')
    #return HttpResponse("Hello, world. You are at chai or django")

def contact(request):
    return HttpResponse("Hello, world. You are at chai or django")

