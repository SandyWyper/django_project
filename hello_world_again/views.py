from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """returns a simple "Hello, World!" response"""
    return HttpResponse("Hello, World! Again!")

    