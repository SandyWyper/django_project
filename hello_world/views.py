from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """returns a simple "Hello, World!" response"""
    if request.method == "GET":
        return HttpResponse("This was a GET request")
    elif request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse("This was a " + request.method + " request")

    