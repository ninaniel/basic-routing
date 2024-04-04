from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def default_greeting(request):
    return HttpResponse("<h1 style='text-align:center; color:green;' >Hello World</h1>")

def greeting(request, name):
    return HttpResponse(f"<h1 style='text-align:center; color:green;' >Hello, {name.capitalize()}</h1>")